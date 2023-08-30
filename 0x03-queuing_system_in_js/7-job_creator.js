const kue = require("kue")

const jobs = [
	{
		phoneNumber: '4153518780',
		message: 'This is the code 1234 to verify your account'
	},
	{
		phoneNumber: '4153518781',
		message: 'This is the code 4562 to verify your account'
	},
	{
		phoneNumber: '4153518743',
		message: 'This is the code 4321 to verify your account'
	},
	{
		phoneNumber: '4153538781',
		message: 'This is the code 4562 to verify your account'
	},
	{
		phoneNumber: '4153118782',
		message: 'This is the code 4321 to verify your account'
	},
	{
		phoneNumber: '4153718781',
		message: 'This is the code 4562 to verify your account'
	},
	{
		phoneNumber: '4159518782',
		message: 'This is the code 4321 to verify your account'
	},
	{
		phoneNumber: '4158718781',
		message: 'This is the code 4562 to verify your account'
	},
	{
		phoneNumber: '4153818782',
		message: 'This is the code 4321 to verify your account'
	},
	{
		phoneNumber: '4154318781',
		message: 'This is the code 4562 to verify your account'
	},
	{
		phoneNumber: '4151218782',
		message: 'This is the code 4321 to verify your account'
	}
];

const queue = kue.createQueue({
	redis: {
		host: '127.0.0.1',
		port: 6379
	}
})

jobs.forEach((v, i, a) => {
	const job = queue.createJob('push_notification_code_2', v).save((err) => {
		if (!err) console.log(`Notification job created: ${job.id}`)
	})
	
	job.on('complete', function(){
		console.log(`Notification job ${job.id} completed`)
	  }).on('failed', function(error){
		console.log(`Notification job ${job.id} failed: ${error}`);
	  }).on('progress', function(progress){
		console.log(`Notification job ${job.id} ${progress}% complete`)
	  });
})

