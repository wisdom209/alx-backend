const createPushNotificationsJobs = (jobs, queue) => {
	if (!Array.isArray(jobs)) throw Error("Jobs is not an array")
	
	jobs.forEach((v, i) => {
		const job = queue.createJob('push_notification_code_3', v).save((err) => {
			if (!err) console.log(`Notification job created: ${job?.id}`)
		})
	
		job?.on('complete', () => {
			console.log(job)
			console.log(`Notification job ${job.id} completed`)
		}).on('failed', function (error) {
			console.log(`Notification job ${job.id} failed: ${error}`);
		}).on('progress', function (progress) {
			console.log(`Notification job ${job.id} ${progress}% complete`)
		});
	})
}

export default createPushNotificationsJobs

