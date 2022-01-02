from fastapi import APIRouter
from typing import Optional
from app.services.daily_services import fetch_daily, fetch_daily_on_full_date, fetch_daily_on_year, fetch_daily_on_year_month
from app.validator.query_validator import validate_daily_format
from app.validator import path_validator

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
    if since is not None:
        validate_daily_format(since)

    if upto is not None:
        validate_daily_format(upto)

    path_validator.validate_year_format(year)

    data = await fetch_daily_on_year(year, since, upto)
    return {
        "ok": True,
        "message": "Data fetched successfully",
        "data": data
    }

@router.get("/daily/{year}/{month}", tags=["daily"])
async def get_daily_data_on_year_month(
    year: str,
    month: str,
    since: Optional[str] = None,
    upto: Optional[str] = None
):
    if since is not None:
        validate_daily_format(since)

    if upto is not None:
        validate_daily_format(upto)
    
    path_validator.validate_year_format(year)
    path_validator.validate_month_format(month)

    data = await fetch_daily_on_year_month(year, month, since, upto)
    return {
        "ok": True,
        "message": "Data fetched successfully",
        "data": data
    }

@router.get("/daily/{year}/{month}/{day}", tags=["daily"])
async def get_daily_data_on_year_month_date(
    year: str,
    month: str,
    day: str
):
    path_validator.validate_year_format(year)
    path_validator.validate_month_format(month)
    path_validator.validate_day_format(day)

    path_validator.validate_full_date(year, month, day)

    data = await fetch_daily_on_full_date(year, month, day)
    return {
        "ok": True,
        "message": "Data fetched successfully",
        "data": data
    }

    return
