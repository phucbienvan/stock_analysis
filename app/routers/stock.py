from fastapi import APIRouter, HTTPException
from app.services.stock_service import StockService
from app.schemas.sche_stock import StockCreateRequest

router = APIRouter()

@router.post("/stock", tags=[""], description="")
async def create(request_data: StockCreateRequest):
    try:
        result = StockService.create(request_data)

        
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
