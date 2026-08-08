from fastapi import FastAPI, HTTPException #fastapi framwork that used to create this API
from pydantic import BaseModel #pydantic library to send requests in json format

app = FastAPI()



#root func
@app.get("/")
async def root():
    return {"message":"Hello Server"}

