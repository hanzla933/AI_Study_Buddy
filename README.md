# AI Study Buddy

A small study app that will answer questions using materials you provide. We are building it one step at a time.

## Current starter

- FastAPI serves a simple welcome page.
- `GET /api/health` confirms that the backend is running.
- PDF processing and AI features are not implemented yet.

## Run locally

From the project folder in PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000 in your browser. The health check is at http://127.0.0.1:8000/api/health.

## Project structure

```text
app/          Backend code
static/       Browser page, styles, and JavaScript
uploads/      Local uploaded study files (ignored by Git)
tests/        Automated tests
```
