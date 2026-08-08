from fastapi import FastAPI, HTTPException #fastapi framwork that used to create this API
from pydantic import BaseModel #pydantic library to send requests in json format

app = FastAPI()



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

