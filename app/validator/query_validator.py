from fastapi import HTTPException
import re
from datetime import datetime

def validate_yearly_format(year_str: str):
    if re.match(r"^\d{4}$", year_str) == None:
        raise HTTPException(status_code=400, detail="Wrong year format on query. Correct format: YYYY (e.g. 2021)")

def validate_monthly_format(month_str: str):
    if re.match(r"^\d{4}\.[0-1]\d$", month_str) == None:
        raise HTTPException(status_code=400, detail="Wrong month format on query. Correct format: YYYY.MM (e.g. 2021.12)")
    
    month_splitted = month_str.split(".")
    month = int(month_splitted[1])
    
    if 1 <= month <= 12:
        raise HTTPException(status_code=400, detail="Month can only be between 01 and 12")

def validate_daily_format(date_str: str):
    if re.match(r"^\d{4}\.[0-1]\d\.[0-3]\d$", date_str) == None:
        raise HTTPException(status_code=400, detail="Wrong date format on query. Correct format: YYYY.MM.DD (e.g. 2021.12.23)")
    
    date_splitted = date_str.split(".")
    year = int(date_splitted[0])
    month = int(date_splitted[1])
    date = int(date_splitted[2])

    if 1 <= month <= 12:
        raise HTTPException(status_code=400, detail="Month can only be between 01 and 12")

    try:
        newDate = datetime(year, month, date)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date")
