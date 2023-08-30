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
})

const setNewSchool = (schoolName, value) => {
	client.set(schoolName, value, redis.print)
}

const redis_get = promisify(client.get).bind(client)

const displaySchoolValue = async (schoolName) => {
	const data = await redis_get(schoolName)
	console.log(data)
}

