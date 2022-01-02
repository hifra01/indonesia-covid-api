from fastapi import APIRouter
from typing import Optional
from app.services.daily_services import fetch_daily
from app.validator.query_validator import validate_daily_format

router = APIRouter()

@router.get("/daily", tags=["daily"])
async def get_daily_data(
    since: Optional[str] = None,
    upto: Optional[str] = None
):
    if since is not None:
        validate_daily_format(since)

    if upto is not None:
        validate_daily_format(upto)

    data = await fetch_daily(since, upto)
    return {
        "ok": True,
        "message": "Data fetched successfully",
        "data": data
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
