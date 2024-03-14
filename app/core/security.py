from passlib.context import CryptContext
import jwt
from typing import Any, Union
from datetime import datetime, timedelta
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(user_id: Union[int, Any]) -> str:
    expire = datetime.utcnow() + timedelta(
        seconds=settings.ACCESS_TOKEN_EXPIRE_SECONDS
    )
    to_encode = {
        "exp": expire, "user_id": str(user_id)
    }
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.SECURITY_ALGORITHM)
    
    return encoded_jwt
