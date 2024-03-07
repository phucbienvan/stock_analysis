from sqlalchemy import Column, String, Boolean
from app.models.model_base import BareBaseModel

class Users(BareBaseModel):
    full_name = Column(String(255), index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)
