from pydantic import BaseModel

class flat_assign(BaseModel):
    flat_id:int
    user_id:int
    rent:int
    lease_time:int

class flat_assigned(flat_assign):
    id:int
    class Config():
        orm_mode=True
