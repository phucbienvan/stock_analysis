from app.schemas.sche_user import RegisterUserRequest
from pandas_datareader import data
import datetime, json
from fastapi_sqlalchemy import db
from app.models import Users
from app.core.security import get_password_hash

class UserService(object):
    __instance = None

    def __init__(self) -> None:
        pass

    @staticmethod
    def register(request_data: RegisterUserRequest):
        find_user = db.session.query(Users).filter(Users.email == request_data.email).first()

        if find_user :
            raise Exception('Email already exists')

        user = Users(
            full_name = request_data.full_name,
            email = request_data.email,
            hashed_password = get_password_hash(request_data.password),
            is_active = True,
        )

        db.session.add(user)
        db.session.commit()

        return user
