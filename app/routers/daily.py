from fastapi import APIRouter
from typing import Optional
from app.services.case_data import fetch_daily

router = APIRouter()

@router.get("/daily", tags=["daily"])
async def get_daily_data(
    since: Optional[str] = None,
    upto: Optional[str] = None
):
    case_data = await fetch_daily(since, upto)
    return {
        "ok": True,
        "message": "Data fetched successfully",
        "data": case_data
    }

@router.get("/daily/{year}", tags=["daily"])
async def get_daily_data_on_year(
    year: str,
    since: Optional[str] = None,
    upto: Optional[str] = None
):
    return

@router.get("/daily/{year}/{month}", tags=["daily"])
async def get_daily_data_on_year_month(
    year: str,
    month: str,
    since: Optional[str] = None,
    upto: Optional[str] = None
):
    return

@router.get("/daily/{year}/{month}/{date}", tags=["daily"])
async def get_daily_data_on_year_month_date(
    year: str,
    month: str,
    date: str
):
    return
