from app.schemas.sche_user import RegisterUserRequest
from pandas_datareader import data
import datetime, json
from fastapi_sqlalchemy import db
from app.models import Users

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
            hashed_password = 123456,
            is_active = True,
        )

        db.session.add(user)
        db.session.commit()

        return user
