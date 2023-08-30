const { createClient } = require("redis");
const client = createClient()

client.subscribe("holberton school channel")

client.on('error', err => console.log("Redis client not connected to the server: ERROR_MESSAGE"))

client.on('connect', () => {
	console.log("Redis client connected to the server")
})

client.on('message', (channel, message) => {
	console.log(channel, ":", message)

	if (message == "KILL_SERVER"){
		client.unsubscribe("holberton school channel")
		client.quit()
	}
})




