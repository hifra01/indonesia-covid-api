import aiohttp
from datetime import datetime
from functools import reduce
from app.configs import datasource

async def __get_case_data(session: aiohttp.ClientSession):
    async with session.get(datasource.case_update_url) as response:
        data = await response.json()
    return data

async def __get_vaccine_data(session: aiohttp.ClientSession):
    async with session.get(datasource.vaccine_update_url) as response:
        data = await response.json()
    return data

async def fetch_total_data():
    
    async with aiohttp.ClientSession() as session:
        case_data = await __get_case_data(session)
        vaccine_data = await __get_vaccine_data(session)

    data = {
        "total_positive": case_data["update"]["total"]["jumlah_positif"],
        "total_recovered": case_data["update"]["total"]["jumlah_sembuh"],
        "total_deaths": case_data["update"]["total"]["jumlah_meninggal"],
        "total_active": case_data["update"]["total"]["jumlah_dirawat"],
        "total_vaccination_1": vaccine_data["vaksinasi"]["total"]["jumlah_vaksinasi_1"],
        "total_vaccination_2": vaccine_data["vaksinasi"]["total"]["jumlah_vaksinasi_2"],
        "new_positive": case_data["update"]["penambahan"]["jumlah_positif"],
        "new_recovered": case_data["update"]["penambahan"]["jumlah_sembuh"],
        "new_deaths": case_data["update"]["penambahan"]["jumlah_meninggal"],
        "new_active": case_data["update"]["penambahan"]["jumlah_dirawat"],
        "new_vaccination_1": vaccine_data["vaksinasi"]["penambahan"]["jumlah_vaksinasi_1"],
        "new_vaccination_2": vaccine_data["vaksinasi"]["penambahan"]["jumlah_vaksinasi_2"],
    }

    return data

async def fetch_yearly_data():

    def __parse_year(key: int):
        timestamp = key/1000
        return datetime.utcfromtimestamp(timestamp).year
    
    async with aiohttp.ClientSession() as session:
        case_data = await __get_case_data(session)
        vaccine_data = await __get_vaccine_data(session)

    yearly_data = []

    years = set(map(lambda data: __parse_year(data["key"]), case_data["update"]["harian"]))
    
    for year in years:
        cases_on_year = list(filter(lambda case: __parse_year(case["key"]) == year, case_data["update"]["harian"]))
        positive = sum([case["jumlah_positif"]["value"] for case in cases_on_year])
        recovered = sum([case["jumlah_sembuh"]["value"] for case in cases_on_year])
        deaths = sum([case["jumlah_meninggal"]["value"] for case in cases_on_year])

        # active cases still in doubt because of negative value
        active = sum([case["jumlah_dirawat"]["value"] for case in cases_on_year])

        yearly_data.append({
            "year": str(year),
            "positive": positive,
            "recovered": recovered,
            "deaths": deaths,
            "active": active
        })

    return yearly_data
        

