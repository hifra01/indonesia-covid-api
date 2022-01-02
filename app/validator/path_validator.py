from fastapi import HTTPException
import re
from datetime import datetime, timezone

def validate_year_format(year: str):
    if re.match(r"^\d{4}$", year) == None:
        raise HTTPException(status_code=400, detail="Wrong year format on path. Correct format: YYYY (e.g. 2021)")
    
    year_int = int(year)

    if year_int < 1970:
        raise HTTPException(status_code=400, detail="Year can only start from 1970")

def validate_month_format(month: str):
    if re.match(r"^[0-1]\d$", month) == None:
        raise HTTPException(status_code=400, detail="Wrong year format on path. Correct format: MM (e.g. 05)")

    month_int = int(month)

    if month < 1 or month > 12:
        raise HTTPException(status_code=400, detail="Month can only be between 01 and 12")

def validate_day_format(day: str):
    if re.match(r"^[0-3]\d$") == None:
        raise HTTPException(status_code=400, detail="Wrong year format on path. Correct format: MM (e.g. 05)")

    day_int = int(day)

    if day < 1 or day > 31:
        raise HTTPException(status_code=400, detail="Day can only be between 01 and 31")

def validate_full_date(year: str, month: str, day: str):
    year_int = int(year)
    month_int = int(month)
    day_int = int(day)

    try:
        new_date = datetime(year_int, month_int, day_int, tzinfo=timezone.utc)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date")
    