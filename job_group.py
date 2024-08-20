from job import Job

class JobGroup:
    def __init__(self):
        self.job_group = []
    
    def add_job(self, job: Job):
        self.job_group.append(job)
