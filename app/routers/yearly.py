from fastapi import APIRouter
from typing import Optional
from app.services.data_fetch import fetch_yearly_data

router = APIRouter()

@router.get("/yearly", tags=["years"])
async def get_yearly_data(since: Optional[str] = None, upto: Optional[str] = None):
    data = await fetch_yearly_data(since, upto)
    return {
        "ok": True,
        "message": "Data fetched successfully",
        "data": data
    }