from fastapi import APIRouter
from typing import Optional
from app.services.data_fetch import fetch_yearly_data, fetch_yearly_data_on_year

router = APIRouter()

@router.get("/yearly", tags=["yearly"])
async def get_yearly_data(since: Optional[str] = None, upto: Optional[str] = None):
    data = await fetch_yearly_data(since, upto)
    return {
        "ok": True,
        "message": "Data fetched successfully",
        "data": data
    }

@router.get("/yearly/{year}", tags=["yearly"])
async def get_yearly_data_on_year(year: int):
    data = await fetch_yearly_data_on_year(year)
    return {
        "ok": True,
        "message": "Data fetched successfully",
        "data": data
    }