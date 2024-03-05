from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/", tags=[""], description="")
async def index():
    try:
        return "hello w"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
