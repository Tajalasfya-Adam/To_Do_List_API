from fastapi import FastAPI, HTTPException, Depends #fastapi framwork that used to create this API
from pydantic import BaseModel #pydantic library to send requests in json format
from sqlmodel import SQLModel, Field, create_engine, Session, select #sqlmodel library responsible of the database
from contextlib import asynccontextmanager
from typing import Optional, List


# bulding the model
class Tasks(SQLModel, table = True): # main model
    id : Optional[int] = Field(default = None, primary_key = True, index = True)
    title : str = Field(index = True)
    done : bool = Field(default=False, index = True)

#responsible of new tasks
class NewTask(SQLModel):
    title:str = Field(index=True)

#responsible of updating tasks
class UpdateTask(SQLModel):
    title:Optional[str] = Field(index = True)

# The API start from here
engine = create_engine("sqlite:///./tasks.db", echo = True) # engine is the object the handles the communication between the API and database

#this is important it check the tasks.db file
@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        statement = select(Tasks)
        results = session.exec(statement).first()

        if not results:
            example_tasks = [
                Tasks(title = "study linear algebra", done = False),
                Tasks(title = "stage 0", done = True),
                Tasks(title = "buy milk", done = False)
            ]
            session.add_all(example_tasks)
            session.commit()
    yield

app = FastAPI(title = "To_Do_List API", lifespan=lifespan)



# to determine when to create the tasks.db file in the harddisk
@app.on_event("startup")
def on_event():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session


class TaskCreate(BaseModel):
    title: str


#root func
@app.get("/", summary="Return a welcome message")
async def root():
    return {"message":"Hello Server"}

#to describe this API
@app.get("/info", summary="Return API metadata and available endpoints")
def describe():
    return { "name": "Task API", "version": "1.0", "endpoints": ["/tasks"] }

#to check the server status
@app.get("/health", summary="Check whether the server is running")
def server_health():
    return { "status": "ok" }



#endpoints start from here

# It returns all the tasks
@app.get("/tasks", response_model=List[Tasks], summary="List all tasks")
def all_tasks(session:Session = Depends(get_session)):
    task = select(Tasks)
    statement = session.exec(task).all()
    return statement

@app.get("/tasks/{id}", response_model=Tasks, summary="Retrieve a specific task by its ID")
async def one_task(id: int, session:Session = Depends(get_session)):
    task = session.get(Tasks, id)
    if not task:
        raise HTTPException(status_code=404, detail={"error": f"Task {id} not found"})
    return task

# Creating new tasks endpoint
@app.post("/tasks", status_code = 201, response_model=Tasks, summary="Create a new task")
async def create_item(payload:NewTask, session:Session=Depends(get_session)):
    if payload.title =="string" or payload.title.strip() == "": #to make sure the title is not empty or "sting"
        raise HTTPException(status_code=400, detail="Title is required")

    new_task = Tasks.model_validate(payload)

    session.add(new_task)
    session.commit()
    session.refresh(new_task)
    return new_task

# Update task's endpoint
@app.put("/tasks/{id}", response_model=Tasks, summary="Update the title of an existing task")
async def updateItem(id: int, title: UpdateTask, session:Session = Depends(get_session)):
    task = session.get(Tasks, id)
    if not task:
        raise HTTPException(status_code=404, detail=f"item {id} not found")
    
    task.title = title.title
    session.add(task)
    session.commit()
    session.refresh(task)
    return task
        
# Delete task's endpoint
@app.delete("/tasks/{id}", status_code=204, summary="Delete a task by its ID")
async def deleteItem(id: int, session:Session = Depends(get_session)):
    task = session.get(Tasks, id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    session.delete(task)
    session.commit()

# ==========================================
#mission completed, a litle celibration (:
# ==========================================
