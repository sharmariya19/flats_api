from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
from typing import List
from database import get_db
from schemas.flat_assignment import flat_assign, flat_assigned
from crud_func.FlatAssignment_fun import flat_assign_details, flatassign, get_details_byID,update_assign, delete_assignment_by_id
router = APIRouter()


@router.get("/flatassign", tags=['flatassign'], response_model=List[flat_assigned],status_code=status.HTTP_200_OK)
def flatassign_details(db:Session = Depends(get_db)):
    details = flat_assign_details(db=db)
    return details

@router.post("/flatassign",tags=['flatassign'], response_model=flat_assigned, status_code=status.HTTP_201_CREATED)
def flatassign_details(detail: flat_assign,db: Session = Depends(get_db)):
    details = flatassign(obj=detail,db=db)
    return details


@router.get("/flatassign/{id}", tags=['flatassign'], response_model=flat_assigned,status_code=status.HTTP_200_OK)
def flatassign_detail(id:int,db:Session = Depends(get_db)):
    detail = get_details_byID(id=id,db=db)
    if not detail:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Details with this id {id} does not exist")
    return detail

@router.put("/flatassign/{id}", tags=['flatassign'], response_model=flat_assigned,status_code=status.HTTP_200_OK)
def update_details(id:int, ref: flat_assign, db:Session = Depends(get_db)):
    flat = update_assign(id=id,obj=ref,db=db)
    return flat


@router.delete("/flatassign/{id}", tags=['flatassign'], status_code=status.HTTP_200_OK) 
def delete_assignment(id: int,db: Session = Depends(get_db)):
    delete_assignment_by_id(id=id,db=db)
    
    return {"msg":"Successfully deleted."}
