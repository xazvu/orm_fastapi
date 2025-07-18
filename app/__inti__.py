from fastapi import APIRouter
from routers.user import router as user_router
from routers.message import router as message_router

router = APIRouter()
router.include_router(user_router)
router.include_router(message_router)