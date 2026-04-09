# Job Tracker API

A FastAPI application to track job applications with PostgreSQL backend.

## Project Status

**Current Phase:** Database integration in progress

- ✅ FastAPI basic setup with CRUD endpoints (in-memory)
- ✅ PostgreSQL connection configured via `.env`
- ✅ SQLAlchemy ORM models defined (`Job_schema`)
- ✅ Database tables created in PostgreSQL
- 🔄 **Next:** Integrate DB models with FastAPI endpoints
- ⏳ Future: Add authentication, job status tracking, application history

## Requirements

- Python 3.9+
- PostgreSQL 12+
- Virtual environment in `.venv`

## Setup

1. **Clone and enter the project directory:**
```bash
cd /Users/benwheeler/Documents/Job-Tracker-SaaS
source .venv/bin/activate
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Configure `.env` file** (in project root):
```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=mydb
DB_USER=benw
DB_PASSWORD=your_password
```

4. **Ensure PostgreSQL is running** and create the database:
```bash
createdb -U postgres mydb
```

5. **Run the app:**
```bash
.venv/bin/python -m uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`
- **Interactive docs:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

## Data Model

**Job Schema (PostgreSQL table)**
- `id` — auto-assigned primary key (INTEGER)
- `name` — job title (VARCHAR, required)
- `company` — company name (VARCHAR(30), required)
- `state` — job location state (VARCHAR, optional)
- `offer` — received offer (BOOLEAN, default=True)

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/job/` | Create a new job |
| GET | `/jobs` | List all jobs |
| GET | `/jobs/{job_id}` | Get a specific job |
| PUT | `/jobs/{job_id}` | Update a job |
| DELETE | `/jobs/{job_id}` | Delete a job |

## Example Requests

**Create a job:**
```bash
curl -X POST "http://127.0.0.1:8000/job/" \
  -H "Content-Type: application/json" \
  -d '{"name":"Backend Engineer","company":"Acme","state":"CA","offer":true}'
```

**List all jobs:**
```bash
curl "http://127.0.0.1:8000/jobs"
```

**Get a specific job:**
```bash
curl "http://127.0.0.1:8000/jobs/1"
```

**Update a job:**
```bash
curl -X PUT "http://127.0.0.1:8000/jobs/1" \
  -H "Content-Type: application/json" \
  -d '{"name":"Senior Backend Engineer","company":"Acme","state":"CA","offer":true}'
```

**Delete a job:**
```bash
curl -X DELETE "http://127.0.0.1:8000/jobs/1"
```

## Project Structure

```
Job-Tracker-SaaS/
├── .env                  # Database credentials (git-ignored)
├── .venv/                # Virtual environment
├── requirements.txt      # Python dependencies
├── README.MD             # This file
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI routes (in-memory; needs DB integration)
│   ├── models.py        # SQLAlchemy ORM models & DB connection
│   └── schemas.py       # Pydantic schemas for request/response validation
```

## Notes

- **Current state:** Endpoints use in-memory `jobs` list; PostgreSQL tables exist but are not yet queried
- **Next step:** Replace in-memory operations with SQLAlchemy session queries
- **Database:** Tables are auto-created on app startup via `Base.metadata.create_all(engine)`
- **Credentials:** Never commit `.env` file; it's in `.gitignore`