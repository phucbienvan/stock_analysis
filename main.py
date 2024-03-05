import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Import the CORSMiddleware
from fastapi_sqlalchemy import DBSessionMiddleware

from app.routers import stock
from app.models import Base
from app.db.base import engine
from app.core.config import settings

Base.metadata.create_all(bind=engine)


def get_application() -> FastAPI:
    application = FastAPI(
        title=settings.PROJECT_NAME,
        description=''
    )
    
    application.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    application.add_middleware(DBSessionMiddleware, db_url=settings.DATABASE_URL)
    application.include_router(stock.router)

    return application


app = get_application()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8989, reload=True, log_level="info")
