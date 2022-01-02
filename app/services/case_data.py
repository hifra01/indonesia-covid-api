import aiohttp
import re

from functools import reduce
from app.configs import datasource
from app.utils.utils import parse_year, parse_month, parse_day

async def __get_case_data(session: aiohttp.ClientSession):
    async with session.get(datasource.case_update_url) as response:
        data = await response.json()
    return data

def __sum_data_on_year(year: int, cases):
    cases_on_year = list(filter(lambda case: parse_year(case["key"]) == year, cases))
    positive = sum([case["jumlah_positif"]["value"] for case in cases_on_year])
    recovered = sum([case["jumlah_sembuh"]["value"] for case in cases_on_year])
    deaths = sum([case["jumlah_meninggal"]["value"] for case in cases_on_year])

    # active cases still in doubt because of negative value
    active = sum([case["jumlah_dirawat"]["value"] for case in cases_on_year if case["jumlah_dirawat"]["value"] > 0])

    return {
        "year": str(year),
        "positive": positive,
        "recovered": recovered,
        "deaths": deaths,
        "active": active
    }

def __collect_data_on_year(year: int, cases):
    return list(filter(lambda case: parse_year(case["key"]) == year, cases))

def __collect_data_on_month(month: int, cases):
    return list(filter(lambda case: parse_month(case["key"]) == month, cases))

def __sum_data_on_month(month: str, cases):
    splitted_month_str = month.split("-")
    case_year = int(splitted_month_str[0])
    case_month = int(splitted_month_str[1])
    yearly_cases = __collect_data_on_year(case_year, cases)
    monthly_cases = __collect_data_on_month(case_month, yearly_cases)

    positive = sum([case["jumlah_positif"]["value"] for case in monthly_cases])
    recovered = sum([case["jumlah_sembuh"]["value"] for case in monthly_cases])
    deaths = sum([case["jumlah_meninggal"]["value"] for case in monthly_cases])

    # active cases still in doubt because of negative value
    active = sum([case["jumlah_dirawat"]["value"] for case in monthly_cases if case["jumlah_dirawat"]["value"] > 0])

    return {
        "month": month,
        "positive": positive,
        "recovered": recovered,
        "deaths": deaths,
        "active": active
    }

def __sum_data(cases):
    positive = sum([case["jumlah_positif"]["value"] for case in cases])
    recovered = sum([case["jumlah_sembuh"]["value"] for case in cases])
    deaths = sum([case["jumlah_meninggal"]["value"] for case in cases])

    # active cases still in doubt because of negative value
    active = sum([case["jumlah_dirawat"]["value"] for case in cases if case["jumlah_dirawat"]["value"] > 0])

    return {
        "positive": positive,
        "recovered": recovered,
        "deaths": deaths,
        "active": active
    }


async def fetch_yearly(since, upto):
    yearly_since, yearly_upto = None, None

    if since != None:
        if re.match(r"\d{4}", since):
            yearly_since = int(since)

    if upto != None:
        if re.match(r"\d{4}", upto):
            yearly_upto = int(upto)

    async with aiohttp.ClientSession() as session:
        case_data = await __get_case_data(session)

    daily_data = case_data["update"]["harian"]

    years = set(map(lambda data: parse_year(data["key"]), daily_data))

    if yearly_since != None:
        years = list(filter(lambda year: year >= yearly_since, years))

    if yearly_upto != None:
        years = list(filter(lambda year: year <= yearly_upto, years))

    yearly_data = []

    for year in years:
        yearly_data.append(__sum_data_on_year(year, daily_data))

    return yearly_data

async def fetch_yearly_on_year(year: int):

    async with aiohttp.ClientSession() as session:
        case_data = await __get_case_data(session)
    
    daily_data = case_data["update"]["harian"]

    return __sum_data_on_year(year, daily_data)

async def fetch_monthly(since, upto):
    async with aiohttp.ClientSession() as session:
        case_data = await __get_case_data(session)
    
    daily_data = case_data["update"]["harian"]

    monthly_data = []

    months = sorted(
        set(
            map(
                lambda data: str(f"{parse_year(data['key'])}-{parse_month(data['key']):02d}"),
                daily_data
            )
        )
    )

    for month in months:
        monthly_data.append(__sum_data_on_month(month, daily_data))

    return monthly_data

async def fetch_monthly_on_year(year, since, upto):
    async with aiohttp.ClientSession() as session:
        case_data = await __get_case_data(session)

    case_year = int(year)

    daily_data = case_data["update"]["harian"]

    cases_on_year = list(filter(lambda data: parse_year(data["key"]) == case_year, daily_data ))

    months = sorted(
        set(
            map(
                lambda data: str(f"{parse_year(data['key'])}-{parse_month(data['key']):02d}"),
                cases_on_year
            )
        )
    )
    
    monthly_data = []

    for month in months:
        monthly_data.append(__sum_data_on_month(month, cases_on_year))

    return monthly_data

async def fetch_monthly_on_year_month(year, month):
    async with aiohttp.ClientSession() as session:
        case_data = await __get_case_data(session)

    daily_data = case_data["update"]["harian"]

    case_year = int(year)
    case_month = int(month)


    cases_on_year = list(filter(lambda data: parse_year(data["key"]) == case_year, daily_data ))
    cases_on_month = list(filter(lambda data: parse_month(data["key"]) == case_month, cases_on_year ))

    month_string = f"{int(year)}-{int(month):02d}"

    data = __sum_data(cases_on_month)

    return {
        "month": month_string,
        **data
    }

async def fetch_daily(since, upto):
    async with aiohttp.ClientSession() as session:
        case_data = await __get_case_data(session)

    daily_data = case_data["update"]["harian"]

    daily_cases = []

    for case in daily_data:
        case_year = parse_year(case["key"])
        case_month = parse_month(case["key"])
        case_day = parse_day(case["key"])

        case_date = f"{case_year}-{case_month:02d}-{case_day:02d}"


        positive = case["jumlah_positif"]["value"]
        recovered = case["jumlah_sembuh"]["value"]
        deaths = case["jumlah_meninggal"]["value"]

        # active cases still in doubt because of negative value
        active = case["jumlah_dirawat"]["value"]

        daily_cases.append({
            "date": case_date,
            "positive": positive,
            "recovered": recovered,
            "deaths": deaths,
            "active": active
        })
    
    return daily_cases








