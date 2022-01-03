from fastapi import HTTPException
from datetime import datetime, timezone
from app.services.data_fetcher import daily_cases, daily_vaccines
from app.utils.data_mapper import map_case_to_dict, map_vaccine_to_dict
from app.utils.key_parser import parse_to_full_date_str
from app.utils import data_filter

async def fetch_daily(since, upto):
    case_data = await daily_cases()
    vaccine_data = await daily_vaccines()

    if since is not None:
        case_data = data_filter.daily_since(since, case_data)
        vaccine_data = data_filter.daily_since(since, vaccine_data)

    if upto is not None:
        case_data = data_filter.daily_upto(upto, case_data)
        vaccine_data = data_filter.daily_upto(upto, vaccine_data)

    daily_data = []

    for case in case_data:
        case_key = case["key"]
        mapped_case = map_case_to_dict(case)

        mapped_vaccine = dict()
        vaccine_on_date_list = list(filter(lambda data: data["key"] == case_key, vaccine_data))

        if len(vaccine_on_date_list) > 0:
            vaccine_on_date = vaccine_on_date_list[0]
            mapped_vaccine = map_vaccine_to_dict(vaccine_on_date)

        new_data = {
            "date": parse_to_full_date_str(case_key),
            **mapped_case,
            **mapped_vaccine
        }

        daily_data.append(new_data)
    
    return daily_data

# To fetch daily data on certain year
async def fetch_daily_on_year(year, since, upto):
    case_data = await daily_cases()
    vaccine_data = await daily_vaccines()

    year_int = int(year)

    case_data = data_filter.data_on_year(year_int, case_data)
    vaccine_data = data_filter.data_on_year(year_int, vaccine_data)

    if since is not None:
        case_data = data_filter.daily_since(since, case_data)
        vaccine_data = data_filter.daily_since(since, vaccine_data)

    if upto is not None:
        case_data = data_filter.daily_upto(upto, case_data)
        vaccine_data = data_filter.daily_upto(upto, vaccine_data)
    
    daily_data = []

    for case in case_data:
        case_key = case["key"]
        mapped_case = map_case_to_dict(case)

        mapped_vaccine = dict()
        vaccine_on_date_list = list(filter(lambda data: data["key"] == case_key, vaccine_data))

        if len(vaccine_on_date_list) > 0:
            vaccine_on_date = vaccine_on_date_list[0]
            mapped_vaccine = map_vaccine_to_dict(vaccine_on_date)

        new_data = {
            "date": parse_to_full_date_str(case_key),
            **mapped_case,
            **mapped_vaccine
        }

        daily_data.append(new_data)
    
    return daily_data

# To fetch daily data on certain year and month
async def fetch_daily_on_year_month(year, month, since, upto):
    case_data = await daily_cases()
    vaccine_data = await daily_vaccines()

    year_int = int(year)
    month_int = int(month)

    case_data = data_filter.data_on_year(year_int, case_data)
    vaccine_data = data_filter.data_on_year(year_int, vaccine_data)

    case_data = data_filter.data_on_month(month_int, case_data)

    vaccine_data = data_filter.data_on_month(month_int, vaccine_data)

    if since is not None:
        case_data = data_filter.daily_since(since, case_data)
        vaccine_data = data_filter.daily_since(since, vaccine_data)

    if upto is not None:
        case_data = data_filter.daily_upto(upto, case_data)
        vaccine_data = data_filter.daily_upto(upto, vaccine_data)
    
    daily_data = []

    for case in case_data:
        case_key = case["key"]
        mapped_case = map_case_to_dict(case)

        mapped_vaccine = dict()
        vaccine_on_date_list = list(filter(lambda data: data["key"] == case_key, vaccine_data))

        if len(vaccine_on_date_list) > 0:
            vaccine_on_date = vaccine_on_date_list[0]
            mapped_vaccine = map_vaccine_to_dict(vaccine_on_date)

        new_data = {
            "date": parse_to_full_date_str(case_key),
            **mapped_case,
            **mapped_vaccine
        }

        daily_data.append(new_data)
    
    return daily_data

async def fetch_daily_on_full_date(year, month, day):
    case_data = await daily_cases()
    vaccine_data = await daily_vaccines()

    year_int = int(year)
    month_int = int(month)
    day_int = int(day)

    case_data = data_filter.data_on_full_date(
        year_int,
        month_int,
        day_int,
        case_data
    )

    if len(case_data) == 0:
        raise HTTPException(status_code=404, detail="Data not found")

    vaccine_data = data_filter.data_on_full_date(
        year_int,
        month_int,
        day_int,
        vaccine_data
    )

    mapped_case = map_case_to_dict(case_data[0])
    mapped_vaccine = dict()

    if len(vaccine_data) > 0:
        mapped_vaccine = map_vaccine_to_dict(vaccine_data[0])

    full_date_in_ms = int(datetime(year_int, month_int, day_int, tzinfo=timezone.utc).timestamp() * 1000)

    return {
        "date": parse_to_full_date_str(full_date_in_ms),
        **mapped_case,
        **mapped_vaccine
    }
