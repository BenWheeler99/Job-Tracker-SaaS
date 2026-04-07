from fastapi import FastAPI
from app.schemas import Job

app = FastAPI()

jobs = []
job_id_counter = 1

# This creates a job in the jobs list. uses the schemas model from schemas.py
# also assigns a unique id to each job for indexing latter 
@app.post("/job/")
def create_job(job: Job):
    global job_id_counter
    job_data = job.model_dump()
    job_data["id"] = job_id_counter
    jobs.append(job_data)
    job_id_counter += 1
    return job_data

# This grabs everything in the jobs list and returns it to the webpage
@app.get("/jobs")
def get_jobs(jobs: str):
    return jobs

# This grabs the job by job_id
@app.get("/jobs/{job_id}")
def get_job_by_id(job_id: int):
    job = find_job(job_id)
    return job

# This deletes the job by job_id
@app.delete("/jobs/{job_id}")
def delete_job(job_id: int):
    for index, job in enumerate(jobs):
        if job["id"] == job_id:
            jobs.pop(index)
            return jobs
    return {"error": "Job not found"}

# This is for replacing job info by job_id
@app.put("/jobs/{job_id}")
def update_job(job_id: int, job: Job):
    updated_job = job.model_dump()
    updated_job["id"] = job_id

    for index, existing_job in enumerate(jobs):
        if existing_job["id"] == job_id:
            job[index] = updated_job
            return updated_job
    
    return {"error": "Job not found"}


#call helper
def find_job(job_id: int):
    for index, job in enumerate(jobs):
        if job["id"] == job_id:
            return index, job
    return None, None