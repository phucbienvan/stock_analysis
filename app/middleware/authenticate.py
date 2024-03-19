from fastapi.security import HTTPBearer
import jwt
from app.core.config import settings
from app.schemas.sche_user import TokenPayload
from fastapi import Depends, HTTPException
from pydantic import ValidationError
from fastapi_sqlalchemy import db
from app.models.model_user import Users

reusable_oauth = HTTPBearer(
    scheme_name='Authorization'
)

def authenticate(http_authorization_credentials=Depends(reusable_oauth)):
    try:
        payload = jwt.decode(
            http_authorization_credentials.credentials, settings.SECRET_KEY,
            algorithms=settings.SECURITY_ALGORITHM
        )
        token_data = TokenPayload(**payload)

    except (jwt.PyJWTError, ValidationError):
        raise HTTPException(
            status_code=403,
            detail="credentials"
        )
    user = db.session.query(Users).get(token_data.user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user
