from fastapi import FastAPI
from app.api import task, user
from app.db import engine, Base

app = FastAPI()

# Include the task and user routers
app.include_router(task.router, prefix="/tasks", tags=["tasks"])
app.include_router(user.router, prefix="/users", tags=["users"])

# initialize database
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Management System"}
