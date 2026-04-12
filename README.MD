# Job Tracker API

A FastAPI application to track job applications with PostgreSQL backend.

## Project Status

**Current Phase:** FastAPI + SQLAlchemy + PostgreSQL integration working

- ✅ Database-backed CRUD endpoints are implemented
- ✅ Session dependency (`get_session`) is wired into routes
- ✅ Table auto-creation on startup via `Base.metadata.create_all(bind=engine)`
- ✅ `.env`-driven PostgreSQL configuration

## Requirements

- Python 3.9+
- PostgreSQL 12+
- Virtual environment in `.venv`

## Setup

1. **Clone and enter the project directory:**
```bash
cd /Users/benjaminwheeler/Documents/Job-Tracker-SaaS
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
DB_NAME=your_database_name
DB_USER=your_postgres_role
DB_PASSWORD=your_password
```

4. **Ensure PostgreSQL is running** and create the database:
```bash
createdb -U your_postgres_role your_database_name
```

5. **Run the app:**
```bash
uvicorn app.main:app --port 8001 --reload
```

The API will be available at `http://127.0.0.1:8001`
- **Interactive docs:** http://127.0.0.1:8001/docs
- **ReDoc:** http://127.0.0.1:8001/redoc

## Data Model

**Job Schema (PostgreSQL table)**
- `id` — auto-assigned primary key (INTEGER)
- `name` — job title (VARCHAR, required)
- `company` — company name (VARCHAR(30))
- `state` — one of `applied`, `Rejected`, `offered`
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
curl -X POST "http://127.0.0.1:8001/job/" \
  -H "Content-Type: application/json" \
  -d '{"name":"Backend Engineer","company":"Acme","state":"applied","offer":true}'
```

**List all jobs:**
```bash
curl "http://127.0.0.1:8001/jobs"
```

**Get a specific job:**
```bash
curl "http://127.0.0.1:8001/jobs/1"
```

**Update a job:**
```bash
curl -X PUT "http://127.0.0.1:8001/jobs/1" \
  -H "Content-Type: application/json" \
  -d '{"name":"Senior Backend Engineer","company":"Acme","state":"offered","offer":true}'
```

**Delete a job:**
```bash
curl -X DELETE "http://127.0.0.1:8001/jobs/1"
```

## Verify Data In PostgreSQL

```bash
PGPASSWORD=your_password psql -h localhost -p 5432 -U your_postgres_role -d your_database_name \
  -c '\dt' \
  -c 'SELECT id, name, company, state, offer FROM "Jobs" ORDER BY id DESC LIMIT 10;'
```

Note: the model currently sets `__tablename__ = "Jobs"`, so raw SQL must quote it as `"Jobs"` in PostgreSQL.

## Project Structure

```
Job-Tracker-SaaS/
├── .env                  # Database credentials (git-ignored)
├── .venv/                # Virtual environment
├── requirements.txt      # Python dependencies
├── README.MD             # This file
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI routes using SQLAlchemy session
│   ├── database.py      # Engine, Base, and session dependency
│   ├── models.py        # SQLAlchemy ORM model(s)
│   └── schemas.py       # Pydantic request model(s)
```

## Troubleshooting

- `ERROR: role "postgres" does not exist`
  - Your `.env` is pointing to a PostgreSQL user that does not exist locally.
  - Update `DB_USER` to a real local role.
- `Address already in use`
  - Another process is using your port.
  - Stop old uvicorn processes (`pkill -f "uvicorn app.main:app"`) or use a different port.
- Keep `.env` out of git.