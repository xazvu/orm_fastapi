from fastapi import APIRouter
from user import router as user_router
from message import router as message_router

router = APIRouter()
router.include_router(user_router)
router.include_router(message_router)