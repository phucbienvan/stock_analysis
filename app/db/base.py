from typing import Generator
from app.core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pymysql
pymysql.install_as_MySQLdb()

engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator:
    try:
        print(23)
        db = SessionLocal()
        yield db
    finally:
        db.close()
