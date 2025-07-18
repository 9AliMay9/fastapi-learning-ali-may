from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud
from app.schemas.user import User, UserCreate
from app.db import get_db
from app.utils import hash_password


router = APIRouter()


@router.get("/{username}", response_model=User)
def get_user(username: str, db: Session = Depends(get_db)):
    return crud.get_user_by_username(db, username)


@router.post("/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    hashed_pw = hash_password(user.password)
    return crud.create_user(db=db, user=user, hashed_password=hashed_pw)
