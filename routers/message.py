from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.models import Message
from db.engine import get_db
from db.shemas import Cmessage, Rmessage

router = APIRouter(
    prefix="/message",
    tags=["message"]
)

@router.get("/", response_model=list[Rmessage])
async def get_users(db: Session = Depends(get_db)):
    return db.query(Message).all()


@router.post('/', response_model=Cmessage)
async def create_user(message: Cmessage, db: Session = Depends(get_db)):
    message = Message(message=message.message, description=message.description)
    db.add(message)
    db.commit()
    db.refresh(message)
    return message