from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
from app.schemas import Job
from app.database import engine, Base, get_session
from app.models import Job_schema


#triggering FASTAPI
app = FastAPI()


@app.on_event("startup")
def on_startup():
    # Importing models before create_all ensures metadata has table definitions.
    Base.metadata.create_all(bind=engine)

# This creates a job in the jobs list. uses the schemas model from schemas.py
# also assigns a unique id to each job for indexing latter 
@app.post("/job/")
def create_job(job: Job, db: Session = Depends(get_session)):
    job_data = job.model_dump(exclude={"id"})
    db_job = Job_schema(**job_data)
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job


# This grabs everything in the jobs list and returns it to the webpage
@app.get("/jobs")
def get_jobs(db: Session = Depends(get_session)):
    result = db.execute(select(Job_schema))
    return result.scalars().all()
'''
# This grabs the job by job_id
@app.get("/jobs/{job_id}")
def get_job_by_id(job_id: int):
    for index, job in enumerate(jobs):
        if job["id"] == job_id:
            return index, job

# This deletes the job by job_id
@app.delete("/jobs/{job_id}")
def delete_job(job_id: int):
    for index, job in enumerate(jobs):
        if job["id"] == job_id:
            jobs.pop(index)
            return jobs
    raise HTTPException(status_code=404, detail="Job not found")

# This is for replacing job info by job_id
@app.put("/jobs/{job_id}")
def update_job(job_id: int, job: Job):
    updated_job = job.model_dump()
    updated_job["id"] = job_id

    for index, existing_job in enumerate(jobs):
        if existing_job["id"] == job_id:
            jobs[index] = updated_job
            return updated_job
    
    raise HTTPException(status_code=404, detail="Job not found")'''



