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

## Run The App (Backend + Frontend)

Run both servers at the same time.

1. Start backend (terminal 1, project root):

```bash
source .venv/bin/activate
uvicorn app.main:app --port 8001 --reload
```

2. Start frontend (terminal 2):

```bash
cd client
npm start
```

3. Open the frontend:

- http://localhost:3000

4. Backend API/docs:

- API base URL: http://127.0.0.1:8001
- Swagger docs: http://127.0.0.1:8001/docs
- ReDoc: http://127.0.0.1:8001/redoc

## Frontend Configuration

The frontend uses this environment variable:

- `REACT_APP_API_BASE_URL` (optional)

Default value (if not set):

- `http://127.0.0.1:8001`

Example:

```bash
cd client
REACT_APP_API_BASE_URL=http://127.0.0.1:8001 npm start
```

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
  - Backend is not running on port 8001.
  - Start `uvicorn app.main:app --port 8001 --reload` and retry.
- Port in use:
  - Stop old process or run backend on a different port and update `REACT_APP_API_BASE_URL`.
- PostgreSQL role/database issues:
  - Verify `.env` values match your local PostgreSQL setup.