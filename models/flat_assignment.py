from database import Base
from sqlalchemy import Column, Integer, ForeignKey


class FlatAssignment(Base):
    __tablename__ = "flat_assignment"

    id = Column(Integer,primary_key=True,index=True)
    flat_id = Column(Integer,ForeignKey("flats.id"))
    user_id = Column(Integer,ForeignKey("users.id"))
    rent = Column(Integer)
    lease_time = Column(Integer)
  