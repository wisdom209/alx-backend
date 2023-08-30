const { createClient } = require("redis");
const redis = require("redis")

const client = createClient()

client.on('error', err => console.log("Redis client not connected to the server: ERROR_MESSAGE"))

client.on('connect', () => {
	console.log("Redis client connected to the server")
	displaySchoolValue('Holberton');
	setNewSchool('HolbertonSanFrancisco', '100');
	displaySchoolValue('HolbertonSanFrancisco');
})

const setNewSchool = (schoolName, value) => {
	client.set(schoolName, value, redis.print)
}

const displaySchoolValue = (schoolName) => {
	client.get(schoolName, (err, data) => {
		if (err) console.log(err)
		else console.log(data)
	})
}
