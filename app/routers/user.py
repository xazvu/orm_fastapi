from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from db.models import User
from db.engine import get_db
from db.shemas import CUser, UserR

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.get("/", response_model=list[UserR])
async def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.post('/', response_model=CUser)
async def create_user(user: CUser, db: Session = Depends(get_db)):
    user = User(name=user.name, age=user.age, city=user.city)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user