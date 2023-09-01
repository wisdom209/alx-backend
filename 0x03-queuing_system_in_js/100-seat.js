const redis = require('redis')
const { promisify } = require('util')
const kue = require('kue')
const express = require('express')
const available_seats_key = 'available_seats'

const client = redis.createClient()
const redisAsyncGetClient = promisify(client.get).bind(client)
let reservationEnabled = false

const reserveSeat = (number) => {
	client.set('available_seats', number)
}

const getCurrentAvailableSeats = async () => {
	const current_avail_seats = await redisAsyncGetClient(available_seats_key)
	return current_avail_seats;
}

const queue = kue.createQueue({
	redis: {
		host: '127.0.0.1',
		port: 6379
	}
})


const app = express()
const port = 1245


app.get('/available_seats', async (req, res) => {
	const numberOfAvailableSeats = await getCurrentAvailableSeats()
	res.send({ numberOfAvailableSeats })

})

app.get('/reserve_seat', (req, res) => {
	if (!reservationEnabled)
		return res.send({ "status": "Reservation are blocked" })

	const job = queue.createJob('reserve_seat').save((err) => {
		if (!err) {
			res.send({ "status": "Reservation in process" })
		} else {
			return res.send({ "status": "Reservation failed" })
		}
	})

	job.on('complete', () => {
		console.log(`Seat reservation job ${job.id} completed`)
	}).on('failed', (error) => {
		console.log(`reservation job ${job.id} failed: ${error}`)
	})
})

app.get('/process', (req, res) => {
	res.send({"status":"Queue processing"})
	queue.process('reserve_seat', async(job, done) => {
		let available_seats = await getCurrentAvailableSeats()
		available_seats -= 1
		reserveSeat(available_seats)
		if (available_seats == 0){
			reservationEnabled = false
		}
		if (available_seats >= 0){
			done()
		}else{
			done(Error("Not enough seats available"))
		}
	})
})


client.on('connect', () => {
	client.set(available_seats_key, 50)
	reservationEnabled = true

	app.listen(port, 'localhost')
})


