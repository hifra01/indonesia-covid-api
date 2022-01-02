from fastapi import APIRouter
from typing import Optional
from app.validator.query_validator import validate_monthly_format
from app.validator.path_validator import validate_year_format, validate_month_format
from app.services.monthly_services import fetch_monthly, fetch_monthly_on_year, fetch_monthly_on_month

router = APIRouter()

@router.get("/monthly", tags=["monthly"])
async def get_monthly_data(since: Optional[str] = None, upto: Optional[str] = None):

    if since is not None:
        validate_monthly_format(since)
    
    if upto is not None:
        validate_monthly_format(upto)

    data = await fetch_monthly(since, upto)
    return {
        "ok": True,
        "message": "Data fetched successfully",
        "data": data
    }

@router.get("/monthly/{year}", tags=["monthly"])
async def get_monthly_data_on_year(year: str, since: Optional[str] = None, upto: Optional[str] = None):

    validate_year_format(year)

    if since is not None:
        validate_monthly_format(since)
    
    if upto is not None:
        validate_monthly_format(upto)

    data = await fetch_monthly_on_year(year, since, upto)
    return {
        "ok": True,
        "message": "Data fetched successfully",
        "data": data
    }

@router.get("/monthly/{year}/{month}", tags=["monthly"])
async def get_monthly_data_on_year_month(year: str, month: str):

    validate_year_format(year)
    validate_month_format(month)

    data = await fetch_monthly_on_month(year, month)
    return {
        "ok": True,
        "message": "Data fetched successfully",
        "data": data
    }
