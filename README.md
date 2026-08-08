date: Fri, 07 Aug 2026 03:45:00 GMT
# Task Manager API 🚀

A small RESTful Task Manager API built with FastAPI and Python. Use it to create, read, update, and delete simple todo items while exploring FastAPI features and the auto-generated documentation.

---

## Features

- Minimal, dependency-free task storage (in-memory list).
- CRUD endpoints for managing tasks: list, retrieve, create, update, delete.
- Interactive API docs (Swagger UI and ReDoc) when the server is running.

## Prerequisites

- Python 3.8+
- pip

## Install & Run

Install the runtime dependencies and start the development server:

```bash
pip install fastapi uvicorn pydantic
uvicorn main:app --reload
```

The server will run at http://127.0.0.1:8000 by default.

## Endpoints (summary)

- `GET /` — Return a welcome message.
- `GET /health` — Check whether the server is running.
- `GET /tasks` — List all tasks.
- `GET /tasks/{id}` — Retrieve a specific task by its ID.
- `POST /tasks` — Create a new task (JSON body: `{"title": "Your title"}`).
- `PUT /tasks/{id}` — Update the title of an existing task (use query param `?title=...`).
- `DELETE /tasks/{id}` — Delete a task by its ID.

> Note: This project uses an in-memory list for tasks, so data resets when the server restarts.

## Examples

- List tasks

```bash
curl http://127.0.0.1:8000/tasks
```

- Get a single task

```bash
curl http://127.0.0.1:8000/tasks/1
```

- Create a task

```bash
curl -i -X POST "http://127.0.0.1:8000/tasks" -H "Content-Type: application/json" -d '{"title": "Learn FastAPI"}'
```

- Update a task's title (query parameter)

```bash
curl -X PUT "http://127.0.0.1:8000/tasks/1?title=New%20Title"
```

- Delete a task

```bash
curl -i -X DELETE "http://127.0.0.1:8000/tasks/1"
```

## Interactive Documentation

FastAPI provides interactive docs at:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Contributing

Contributions are welcome. If you fix bugs or improve the API, open a PR or send a patch and describe the change.