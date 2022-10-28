from fastapi import APIRouter, Depends, status
from schemas.user import UserCreate
from database import get_db
from sqlalchemy.orm import Session
from schemas.user import ShowUser
from crud_func.Users_fun import create_new_user, get_all_users
from typing import List

router = APIRouter()

@router.post("/user", tags = ['user'],response_model = ShowUser , status_code=status.HTTP_201_CREATED)
def create_user(user : UserCreate,db: Session = Depends(get_db)):
    user = create_new_user(user=user,db=db)
    return user 

@router.get("/user", tags = ['user'],response_model = List[ShowUser] , status_code=status.HTTP_200_OK)
def get_users(db:Session = Depends(get_db)):
    ref = get_all_users(db=db)
    return ref