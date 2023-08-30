const kue = require('kue')

const push_notification_code = kue.createQueue()

const jobData = {
	phoneNumber: "012345",
	message: "Verify your account"
}

const job = push_notification_code.createJob("push_job", jobData).save((err)=>{
	if (err) console.log("Notification job failed")
	else console.log("Notification job created", job.id)
})

