from fastapi import APIRouter
from typing import Optional
from app.services.case_data import fetch_monthly

router = APIRouter()

@router.get("/monthly", tags=["monthly"])
async def get_monthly_data(since: Optional[str] = None, upto: Optional[str] = None):
    case_data = await fetch_monthly(since, upto)
    return {
        "ok": True,
        "message": "Data fetched successfully",
        "data": case_data
    }
