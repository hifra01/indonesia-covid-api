from fastapi import APIRouter
from typing import Optional
from app.services.case_data import fetch_monthly, fetch_monthly_on_year, fetch_monthly_on_year_month

router = APIRouter()

@router.get("/monthly", tags=["monthly"])
async def get_monthly_data(since: Optional[str] = None, upto: Optional[str] = None):
    case_data = await fetch_monthly(since, upto)
    return {
        "ok": True,
        "message": "Data fetched successfully",
        "data": case_data
    }

@router.get("/monthly/{year}", tags=["monthly"])
async def get_monthly_data_on_year(year: str, since: Optional[str] = None, upto: Optional[str] = None):
    case_data = await fetch_monthly_on_year(year, since, upto)
    return {
        "ok": True,
        "message": "Data fetched successfully",
        "data": case_data
    }

@router.get("/monthly/{year}/{month}", tags=["monthly"])
async def get_monthly_data_on_year_month(year: str, month: str):
    case_data = await fetch_monthly_on_year_month(year, month)
    return {
        "ok": True,
        "message": "Data fetched successfully",
        "data": case_data
    }
    return
