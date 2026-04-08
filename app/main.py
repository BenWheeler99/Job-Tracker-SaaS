from fastapi import FastAPI, HTTPException
from app.schemas import Job
from sqlalchemy import create_engine, text 

# This is the SQLAlchemy create engine command that will use a sqlite data schema
# and store the info in memory. Echo prompts the terminal/logger to confirm commands as ran
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

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
def get_jobs():
    return jobs

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
    
    raise HTTPException(status_code=404, detail="Job not found")


#SQL Engine Section 
'''This creates an engine object and the engine object creates a database and a table
Then we execute a command that INSERTs data into the table and commits it
Committing allows us to build a database that can go on to accept more transactions
This runs everytime we start the application and only saves the data in memory.
'''
with engine.connect() as conn:
    result = conn.execute(text("CREATE TABLE some_table (x int, y int)"))
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
        )
    conn.commit()

# using engine.begin will auto commit if the query passes
with engine.begin() as conn:
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 6, "y": 8}, {"x": 9, "y": 10}],
    )

# This statement just selects data from the database and prints it
with engine.connect() as conn:
    result = conn.execute(text("SELECT x, y FROM some_table"))
    for row in result:
        print(f"x: {row.x}  y: {row.y}")