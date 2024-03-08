from fastapi import APIRouter, HTTPException, Depends
from app.schemas.sche_user import RegisterUserRequest
from typing import Any
from app.services.user_service import UserService
from app.schemas.sche_base import DataResponse

router = APIRouter()

@router.post("/register", tags=[""], description="Register user")
async def register(request_data: RegisterUserRequest, user_service: UserService = Depends())-> Any:
    try:
        register_user = user_service.register(request_data)

        return DataResponse().success_response(data=register_user)
    except Exception as e:
        raise e
