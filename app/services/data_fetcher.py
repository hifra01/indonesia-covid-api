import aiohttp
from app.configs import datasource

async def __get_case_data():
    async with aiohttp.ClientSession() as session:
        async with session.get(datasource.case_update_url) as response:
            data = await response.json()
    return data

async def __get_vaccine_data():
    async with aiohttp.ClientSession() as session:
        async with session.get(datasource.vaccine_update_url) as response:
            data = await response.json()
    return data

async def daily_cases():
    data = await __get_case_data()
    return data["update"]["harian"]

async def daily_vaccines():
    data = await __get_vaccine_data()
    return data["vaksinasi"]["harian"]