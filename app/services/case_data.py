import aiohttp
import re

from functools import reduce
from app.configs import datasource
from app.utils.utils import parse_year

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

    years = set(map(lambda data: parse_year(data["key"]), case_data["update"]["harian"]))

    if yearly_since != None:
        years = list(filter(lambda year: year >= yearly_since, years))

    if yearly_upto != None:
        years = list(filter(lambda year: year <= yearly_upto, years))

    yearly_data = []

    for year in years:
        yearly_data.append(__sum_data_on_year(year, case_data["update"]["harian"]))

    return yearly_data

async def fetch_yearly_on_year(year: int):

    async with aiohttp.ClientSession() as session:
        case_data = await __get_case_data(session)

    return __sum_data_on_year(year, case_data["update"]["harian"])