from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.models import User
from db.engine import get_db
from db.shemas import CUser, UserR
from db import orm_query

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.get("/")
async def get_users(db: Session = Depends(get_db)):
    return orm_query.get_activities(session=db)

@router.get("/user/{id}")
async def get_user_id(activity_id:int, db: Session = Depends(get_db)):
    return orm_query.get_user_by_id(activity_id=activity_id, session=db)



@router.post('/', response_model=UserR)
async def create_user(user: CUser, db: Session = Depends(get_db)):
    user = User(name=user.name, age=user.age, city=user.city)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user