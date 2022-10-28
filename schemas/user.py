from pydantic import BaseModel, EmailStr



class UserCreate(BaseModel):
    username: str
    email : EmailStr
    password : str
    is_superuser : bool


class ShowUser(BaseModel):  
    username : str 
    email : EmailStr
    is_superuser : bool
    class Config():  
        orm_mode = True
