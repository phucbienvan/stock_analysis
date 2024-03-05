import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = os.getenv('PROJECT_NAME', 'STOCK_ANALYSIS')
    SECRET_KEY: str = os.getenv('SECRET_KEY', '')
    API_PREFIX: str = ''
    BACKEND_CORS_ORIGINS: list = ['*']
    DATABASE_URL: str = os.getenv('DATABASE_URL', '')
    ACCESS_TOKEN_EXPIRE_SECONDS: int = 60 * 60 * 24 * 7  # Token expired after 7 days
    SECURITY_ALGORITHM: str = 'HS256'

settings = Settings()
