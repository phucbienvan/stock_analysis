from pydantic import BaseModel, EmailStr
from typing import Optional

class RegisterUserRequest(BaseModel):
    full_name : str
    email : EmailStr
    password : str
    is_active : Optional[bool] = True
