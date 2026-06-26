import asyncio
from fastapi import FastAPI
import time

app =FastAPI()

@app.get("/")
async def home():
    await asyncio.sleep(3)
    return{
        "message" : "Async API"
    }