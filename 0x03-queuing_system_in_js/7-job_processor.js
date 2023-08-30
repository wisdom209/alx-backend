const { json } = require("express")
const kue = require("kue")
const queue = kue.createQueue({
	redis: {
		host: '127.0.0.1',
		port: 6379
	}
})

const blacklistedNumbers = ['4153518780', '4153518781']

const sendNotification = (phoneNumber, message, job, done) => {
	
	if (blacklistedNumbers.includes(`${phoneNumber}`)) {
		done(new Error(`Phone number ${phoneNumber} is blacklisted`))
		return;
	} else {
		job.progress(0, 50)
		job.progress(50, 100)
		console.log(`Sending notification ${phoneNumber}, with message: ${message}`)
		done()
	}
}

queue.process('push_notification_code_2', 2, (job, done) => {
	sendNotification(job.data.phoneNumber, job.data.message, job, done)
})
