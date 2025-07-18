from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud
from app.schemas.task import Task, TaskCreate
from app.db import get_db


router = APIRouter()


@router.post("/", response_model=Task)
def create_task_endpoint(task: TaskCreate, db: Session = Depends(get_db), user_id: int = 1):
    return crud.create_task(db=db, task=task, user_id=user_id)


@router.get("/", response_model=list[Task])
def get_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_tasks(db=db, skip=skip, limit=limit)

