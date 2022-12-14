from pydantic import BaseModel


class Flat_create(BaseModel):
    status: str
    floor_no: int
    rooms: int
    halls: int
    sqft_area: int
    monthly_rent:int



class show_flat(BaseModel):
    id: int
    status: str
    floor_no: int
    rooms: int
    halls: int
    sqft_area: int
    monthly_rent:int
    class Config:
        orm_mode = True