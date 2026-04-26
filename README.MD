# Job Tracker SaaS

FastAPI + PostgreSQL backend with a lightweight React MVP frontend for managing job applications.

## Project Status

Current phase: MVP complete and usable.

- Backend CRUD API is implemented and database-backed.
- Frontend supports create, list, update, and delete.
- Frontend includes loading, success, and error states.
- CORS is configured for local React development.

## Requirements

- Python 3.9+
- PostgreSQL 12+
- Node.js 18+ and npm
- Virtual environment in `.venv`

## Setup

1. Clone and enter the project directory:

```bash
cd /Users/benjaminwheeler/Documents/Job-Tracker-SaaS
```

2. Install backend dependencies:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

3. Configure `.env` in the project root:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database_name
DB_USER=your_postgres_role
DB_PASSWORD=your_password
```

4. Ensure PostgreSQL is running and create the database:

```bash
createdb -U your_postgres_role your_database_name
```

5. Install frontend dependencies:

```bash
cd client
npm install
cd ..
```

## Run The App

For local development and demos, run both from your terminal:

**Terminal 1 (Backend)** — project root:

```bash
source .venv/bin/activate
uvicorn app.main:app --port 8001 --reload
```

**Terminal 2 (Frontend)**:

```bash
cd client
npm start
```

Then open: **http://localhost:3000**

Backend API docs: **http://127.0.0.1:8001/docs**

## Data Model

Job table fields:

- `id`: auto-assigned primary key
- `name`: job title (required)
- `company`: company name (optional)
- `state`: one of `Applied`, `Rejected`, `Offered`
- `offer`: boolean for offer received

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/job/` | Create a job |
| GET | `/jobs` | List jobs |
| GET | `/jobs/{job_id}` | Get one job |
| PUT | `/jobs/{job_id}` | Update job |
| DELETE | `/jobs/{job_id}` | Delete job |

## Example Requests

Create:

```bash
curl -X POST "http://127.0.0.1:8001/job/" \
  -H "Content-Type: application/json" \
  -d '{"name":"Backend Engineer","company":"Acme","state":"Applied","offer":false}'
```

List:

```bash
curl "http://127.0.0.1:8001/jobs"
```

Update:

```bash
curl -X PUT "http://127.0.0.1:8001/jobs/1" \
  -H "Content-Type: application/json" \
  -d '{"name":"Senior Backend Engineer","company":"Acme","state":"Offered","offer":true}'
```

Delete:

```bash
curl -X DELETE "http://127.0.0.1:8001/jobs/1"
```

## Troubleshooting

- Frontend says "Failed to fetch":
  - Ensure backend is running on port 8001.
  - Check that both servers started without error.
- Port already in use:
  - Stop old processes or use different ports.
- PostgreSQL connection fails:
  - Verify `.env` matches your local PostgreSQL setup.