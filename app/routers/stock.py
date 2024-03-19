from fastapi import APIRouter, HTTPException, Depends
from app.services.stock_service import StockService
from app.schemas.sche_stock import StockCreateRequest
from app.schemas.sche_base import DataResponse
from app.middleware.authenticate import authenticate

router = APIRouter()

@router.post("/stock", tags=["create stock"], description="", dependencies=[Depends(authenticate)])
async def create(request_data: StockCreateRequest):
    try:
        result = StockService.create(request_data)
        
        return DataResponse().success_response(data=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
