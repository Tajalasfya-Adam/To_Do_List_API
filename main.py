from fastapi import FastAPI, HTTPException #fastapi framwork that used to create this API
from pydantic import BaseModel #pydantic library to send requests in json format

app = FastAPI()

#temporary database
tasks = [
    {"id":1, "title":"buy milk", "done":False},
    {"id":2, "title":"get new hair cut", "done":False},
    {"id":3, "title":"wash the dishes", "done":False}

]

class taskCreate(BaseModel):
    title: str = None


#root func
@app.get("/")
async def root():
    return {"message":"Hello Server"}

#to describe this API
@app.get("/")
def describe():
    return { "name": "Task API", "version": "1.0", "endpoints": ["/tasks"] }

#to check the server status
@app.get("/health")
def server_health():
    return { "status": "ok" }

#endpoints start from here

@app.get("/tasks")
def all_tasks():
    return tasks

@app.get("/tasks/{id}")
async def one_task(id: int):
    for task in tasks:
        if task["id"] == id:
            return task
    raise HTTPException(status_code=404, detail={"error": f"Task {id} not found"})

