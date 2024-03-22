from fastapi import APIRouter, HTTPException, Depends
from app.schemas.sche_user import RegisterUserRequest, LoginRequest
from typing import Any
from app.services.user_service import UserService
from app.schemas.sche_base import DataResponse
from app.schemas.sche_user import UserResponse
from app.core.security import create_access_token
from app.helpers.exception_handler import CustomException
router = APIRouter()

@router.post("/register", tags=["create user"], description="Register user", response_model=DataResponse[UserResponse])
async def register(request_data: RegisterUserRequest, user_service: UserService = Depends())-> Any:
    try:
        register_user = user_service.register(request_data)

        return DataResponse().success_response(data=register_user)
    except Exception as e:
        return CustomException(http_code=400, code='400', message=str(e))

@router.post("/login", tags=["login"], description="Login")
async def login(request_data: LoginRequest , user_service: UserService = Depends()):
    try:
        login_user = user_service.login(request_data)
        
        if not login_user:
            raise HTTPException(status_code=400, detail='Incorrect email or password')
        
        return DataResponse().success_response({
            'access_token': create_access_token(user_id=login_user.id)
        })
    except Exception as e:
        raise e
