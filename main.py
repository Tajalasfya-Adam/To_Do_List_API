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
@app.get("/", summary="Return a welcome message")
async def root():
    return {"message":"Hello Server"}

#to describe this API
@app.get("/", summary="Return API metadata and available endpoints")
def describe():
    return { "name": "Task API", "version": "1.0", "endpoints": ["/tasks"] }

#to check the server status
@app.get("/health", summary="Check whether the server is running")
def server_health():
    return { "status": "ok" }

#endpoints start from here

@app.get("/tasks", summary="List all tasks")
def all_tasks():
    return tasks

@app.get("/tasks/{id}", summary="Retrieve a specific task by its ID")
async def one_task(id: int):
    for task in tasks:
        if task["id"] == id:
            return task
    raise HTTPException(status_code=404, detail={"error": f"Task {id} not found"})

#there is a bug here i must check
@app.post("/tasks", status_code = 201, summary="Create a new task")
async def create_item(task: taskCreate):
    if task.title == "" or task.title== "string":
        raise HTTPException(status_code=400, detail=f"Title is requierd")
    else:
        """this list comprehension generates a list full of
          already existed tasks then generate new id number
            by taking the max of them + 1"""
        newId = max([i["id"] for i in tasks], defult=0) + 1 

        newTask = {"title":taskCreate.title,
                "id":newId,  
                "done":False}
        
        tasks.append(newTask)
        return newTask

#i must check
@app.put("/tasks/{id}", summary="Update the title of an existing task")
async def updateItem(id : int, title: str):
    for task in tasks:
        if id == task["id"]:
            tasks.replace(task.title, title)
            return f"item updated"
        else:
            raise HTTPException(status_code=400, detail=f"item {id} not found")

#i must check
@app.delete("/tasks/{id}", status_code=204, summary="Delete a task by its ID")
async def deleteItem(id: int):
    if id == tasks["id"]:
        tasks.remove(id)
        return "success"
    else:
        raise HTTPException(status_code=404, detail="No content")


# ==========================================
#mission completed, a litle celibration (:
# ==========================================
