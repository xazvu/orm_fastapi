from fastapi import Depends
from sqlalchemy.orm import Session
from db.models import User
from db.engine import get_db



def get_activities(
        session: Session = Depends(get_db),
):
    return session.query(User).all()


def get_user_by_id(
        activity_id: int,
        session: Session = Depends(get_db),
):
    return session.query(User).filter(User.id == activity_id).first()