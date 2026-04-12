from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException
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
    # This line is converting the Pydantic model instance (job) into a dictionary 
    # format that can be used to create a new SQLAlchemy model instance.
    job_data = job.model_dump(exclude={"id"})
    db_job = Job_schema(**job_data)
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

# This grabs everything in the jobs list and returns it to the webpage
@app.get("/jobs")
def get_jobs(db: Session = Depends(get_session)):
    # This line is using SQLAlchemy's select function to query all records from the Job_schema table. 
    # The result is then processed to return a list of all job records.
    result = db.execute(select(Job_schema))
    return result.scalars().all()

# This grabs the job by job_id
@app.get("/jobs/{job_id}")
def get_job_by_id(job_id: int, db: Session = Depends(get_session)):
    # This line is using SQLAlchemy's select function to query the Job_schema table for a record 
    # where the id matches the provided job_id. The result is then processed to return a single record or None if no match is found.
    result = db.execute(select(Job_schema).where(Job_schema.id == job_id))
    if not result:
        raise HTTPException(status_code=404, detail="Job not found")
    return result.scalar_one_or_none()

# This deletes the job by job_id
@app.delete("/jobs/{job_id}")
def delete_job(job_id: int, db: Session = Depends(get_session)):
    # use the previously defined get_job_by_id function to check if the job exists before attempting to delete it. 
    # If the job is found, it proceeds to delete it from the database and commits the transaction. 
    # If the job is not found, it raises a 404 HTTP exception.
    job = get_job_by_id(job_id, db)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    db.delete(job)
    db.commit()
    return {"message": "Job deleted successfully"}
    raise HTTPException(status_code=404, detail="Job not found")

# This is for replacing job info by job_id
@app.put("/jobs/{job_id}")
def update_job(job_id: int, job: Job, db: Session = Depends(get_session)):
    # This line is converting the Pydantic model instance (job) into a dictionary format that can be used to update 
    # an existing SQLAlchemy model instance.
    updated_job = job.model_dump(exclude={"id"})
    updated_job["id"] = job_id
    job = get_job_by_id(job_id, db)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    # This loop iterates over the key-value pairs in the updated_job dictionary and uses the setattr function 
    # to update the corresponding attributes of the job instance with the new values.
    for key, value in updated_job.items():
        setattr(job, key, value)

    db.commit()
    db.refresh(job)
    return job
