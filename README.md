# Task Manager API 🚀

A lightweight, high-performance RESTful API built with **FastAPI** and **Python** to manage daily tasks as part of the Backend practice journey.

---

## 🛠️ Installation & Running

Ensure you have Python installed, then install dependencies and start the server using:

```bash
pip install fastapi uvicorn pydantic && uvicorn main:app --reload


The server will start at http://127.0.0.1:8000.

📌API Endpoints
MethodEndpointDescriptionSuccess StatusError StatusGET/API description & version200 OK-GET/healthHealth check endpoint200 OK-GET/tasksFetch all tasks200 OK-GET/tasks/{id}Fetch a single task by ID200 OK404 Not FoundPOST/tasksCreate a new task201 Created400 Bad RequestPUT/tasks/{id}Update task title200 OK400 Bad Request, 404 Not FoundDELETE/tasks/{id}Delete a task by ID204 No Content404 Not Found
🧪 Sample curl -i ResponseCreating a new task:Bashcurl -i -X POST "[http://127.0.0.1:8000/tasks](http://127.0.0.1:8000/tasks)" -H "Content-Type: application/json" -d '{"title": "Learn FastAPI"}'

Output:HTTPHTTP/1.1 201 Created
date: Fri, 07 Aug 2026 03:45:00 GMT
server: uvicorn
content-length: 48
content-type: application/json

{"id":4,"title":"Learn FastAPI","done":false}

📑 Interactive Documentation (Swagger UI)FastAPI automatically generates interactive interactive API documentation.Access it while the server is running at:👉 http://127.0.0.1:8000/docs