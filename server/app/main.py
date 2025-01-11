from fastapi import FastAPI
from pydantic import BaseModel 
from transformers import pipeline

app = FastAPI()

@app.get('/')

async def root():
    return {"msg":"Hello Aryan"}
