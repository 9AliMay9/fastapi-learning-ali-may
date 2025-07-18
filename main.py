from fastapi import FastAPI
import time
import asyncio

app = FastAPI()

@app.get("/sync")
def sync_example():
    time.sleep(2)
    return {"message": "This is a sync endpoint"}

@app.get("/async")
async def async_example():
    await asyncio.sleep(2)
    return {"message": "This is an async endpoint"}

