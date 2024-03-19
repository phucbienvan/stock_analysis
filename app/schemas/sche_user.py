from pydantic import BaseModel, EmailStr
from typing import Optional

class RegisterUserRequest(BaseModel):
    full_name : str
    email : EmailStr
    password : str
    is_active : Optional[bool] = True

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    is_active: bool

class TokenPayload(BaseModel):
    user_id: Optional[int] = None
