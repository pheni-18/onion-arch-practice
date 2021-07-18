from .user import router as user_router
from fastapi import APIRouter


router = APIRouter(prefix='/api')
router.include_router(user_router)
