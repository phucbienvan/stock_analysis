from pydantic import BaseModel
from datetime import datetime

class StockCreateRequest(BaseModel):
    sign: str
    start_date: datetime
    end_date: datetime
