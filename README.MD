# Job Tracker API

Simple FastAPI API to create, read, update, and delete job applications.

## Requirements
- Python 3.9+
- Virtual environment in `.venv`

## Setup
```bash
cd /Users/benwheeler/Documents/Job-Tracker-SaaS
source .venv/bin/activate
pip install fastapi uvicorn pydantic

## RUN COMMAND
.venv/bin/python -m uvicorn app.main:app --reload

Data Model (Job)
id (auto-assigned)
name (required)
company (optional)
state (optional)
offer (optional bool)

Endpoints
POST /job/ — create a job
GET /jobs — list all jobs
GET /jobs/{job_id} — get one job by id
PUT /jobs/{job_id} — replace a job by id
DELETE /jobs/{job_id} — delete a job by id

EXAMPLE 
curl -X POST "http://127.0.0.1:8000/job/" \
  -H "Content-Type: application/json" \
  -d '{"name":"Backend Engineer","company":"Acme","state":"CA","offer":true}'

curl "http://127.0.0.1:8000/jobs"
curl "http://127.0.0.1:8000/jobs/1"

Notes
Data is stored in memory (jobs list), so it resets when the server restarts.