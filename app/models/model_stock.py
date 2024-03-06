from sqlalchemy import Column, String, DateTime

from app.models.model_base import BareBaseModel

class Stock(BareBaseModel):
    sign = Column(String(255), index=True)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    content = Column(String)
