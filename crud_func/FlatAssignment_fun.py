from schemas.flat_assignment import flat_assign
from sqlalchemy.orm import Session
from models.flat_assignment import FlatAssignment
from fastapi import HTTPException,status
from crud_func.Flats_fun import update_status_by_id, check_status


def flatassign(obj: flat_assign,db: Session ):
    if check_status(obj.flat_id, db) is True:
        flat = FlatAssignment(**obj.dict())
        update_status_by_id(flat.flat_id,db, "rented")
        db.add(flat)
        db.commit()
        db.refresh(flat)
        return flat
    else : raise HTTPException(status_code=status.HTTP_202_ACCEPTED, detail=f"Already rented")

def flat_assign_details(db:Session):
    flats=db.query(FlatAssignment).all()
    return flats

def get_details_byID(id:int , db:Session):
    flat=db.query(FlatAssignment).get(id)
    return flat


def delete_assignment_by_id(id: int,db: Session):
    ref = db.query(FlatAssignment).get(id)
    if not ref:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Flat with id {id} not found")
    else:
        update_status_by_id(ref.flat_id,db, "empty")
        db.delete(ref)
    db.commit()


def update_assign(id:int, obj:flat_assign,db:Session):
    checkflat=db.query(FlatAssignment).get(id)
    if (check_status(checkflat.flat_id, db) or checkflat.flat_id == obj.flat_id)is True:
        flat = FlatAssignment(**obj.dict())
        update_status_by_id(flat.flat_id,db, "rented")
        db.add(flat)
        db.commit()
        db.refresh(flat)
        return flat
    else : raise HTTPException(status_code=status.HTTP_202_ACCEPTED, detail=f"Already rented")


# ref = db.query(Flats).get(id)
#     if not ref:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Flat with id {id} not found")
#     else:
#         ref.flat_id=obj.flat_id
#         ref.user_id=obj.user_id
#         ref.rent=obj.rent
#         ref.monthly_rent=obj.monthly_rent
#         ref.sqft_area=obj.sqft_area
#         ref.floor_no=obj.floor_no

#     db.commit()