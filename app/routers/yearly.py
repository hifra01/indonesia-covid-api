from fastapi import APIRouter
from typing import Optional
from app.services.case_data import fetch_yearly, fetch_yearly_on_year
from app.validator.query_validator import validate_yearly_format
from app.validator.path_validator import validate_year_format

router = APIRouter()

@router.get("/yearly", tags=["yearly"])
async def get_yearly_data(since: Optional[str] = None, upto: Optional[str] = None):

    if since != None: validate_yearly_format(since)
    if upto != None: validate_yearly_format(upto)

    case_data = await fetch_yearly(since, upto)
    return {
        "ok": True,
        "message": "Data fetched successfully",
        "data": case_data
    }

@router.get("/yearly/{year}", tags=["yearly"])
async def get_yearly_data_on_year(year: str):
    validate_year_format(year)

    case_data = await fetch_yearly_on_year(year)
    return {
        "ok": True,
        "message": "Data fetched successfully",
        "data": case_data
    }