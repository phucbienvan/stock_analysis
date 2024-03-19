from fastapi import APIRouter
from app.routers import stock, user

router = APIRouter()

router.include_router(stock.router)
router.include_router(user.router)
