const { createClient } = require("redis");
const redis = require("redis")
const { promisify} = require("util")

const client = createClient()

client.on('error', err => console.log("Redis client not connected to the server: ERROR_MESSAGE"))

client.on('connect', async () => {
	console.log("Redis client connected to the server")
	await displaySchoolValue('Holberton');
	setNewSchool('HolbertonSanFrancisco', '100');
	await displaySchoolValue ('HolbertonSanFrancisco');

	client.hset("HolbertonSchools", "Portland", "50", redis.print)
	client.hset("HolbertonSchools", "Seattle", "80", redis.print)
	client.hset("HolbertonSchools", "New York", "20", redis.print)
	client.hset("HolbertonSchools", "Bogota", "20", redis.print)
	client.hset("HolbertonSchools", "Cali", "40", redis.print)
	client.hset("HolbertonSchools", "Paris", "2", redis.print)

	client.hgetall("HolbertonSchools", (error, data) => {
		if(!error)
			console.log(data)
	})
})

const setNewSchool = (schoolName, value) => {
	client.set(schoolName, value, redis.print)
}

const redis_get = promisify(client.get).bind(client)

const displaySchoolValue = async (schoolName) => {
	const data = await redis_get(schoolName)
	console.log(data)
}

