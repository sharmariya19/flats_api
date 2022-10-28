from schemas.user import UserCreate
from hashing import Hasher
from sqlalchemy.orm import Session
from models.user import User

def create_new_user(user:UserCreate,db:Session):
    user = User(username=user.username,
        email = user.email,
        hashed_password= Hasher.get_password_hash(user.password),
        is_superuser=user.is_superuser
        )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_all_users(db:Session):
    obj=db.query(User).all()
    return obj