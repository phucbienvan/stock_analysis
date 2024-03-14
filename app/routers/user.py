from fastapi import APIRouter, HTTPException, Depends
from app.schemas.sche_user import RegisterUserRequest, LoginRequest
from typing import Any
from app.services.user_service import UserService
from app.schemas.sche_base import DataResponse
from app.schemas.sche_user import UserResponse

router = APIRouter()

@router.post("/register", tags=[""], description="Register user", response_model=DataResponse[UserResponse])
async def register(request_data: RegisterUserRequest, user_service: UserService = Depends())-> Any:
    try:
        register_user = user_service.register(request_data)

        return DataResponse().success_response(data=register_user)
    except Exception as e:
        raise e


@router.post("/login", description="Login")
async def login(request_data: LoginRequest , user_service: UserService = Depends()):
    try:
        login_user = user_service.login(request_data)
        
        if not login_user:
            raise HTTPException(status_code=400, detail='Incorrect email or password')
        elif not user.is_active:
            raise HTTPException(status_code=401, detail='Inactive user')
        
    except Exception as e:
        raise e