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

async def total_and_update_cases():
    data = await __get_case_data()
    return {
        "total_positive": data["update"]["total"]["jumlah_positif"],
        "total_recovered": data["update"]["total"]["jumlah_sembuh"],
        "total_deaths": data["update"]["total"]["jumlah_meninggal"],
        "total_active": data["update"]["total"]["jumlah_dirawat"],
        "new_positive": data["update"]["penambahan"]["jumlah_positif"],
        "new_recovered": data["update"]["penambahan"]["jumlah_sembuh"],
        "new_deaths": data["update"]["penambahan"]["jumlah_meninggal"],
        "new_active": data["update"]["penambahan"]["jumlah_dirawat"],
    }

async def total_and_update_vaccines():
    data = await __get_vaccine_data()
    return {
        "total_vaccinated_1": data["vaksinasi"]["total"]["jumlah_vaksinasi_1"],
        "total_vaccinated_2": data["vaksinasi"]["total"]["jumlah_vaksinasi_2"],
        "new_vaccinated_1": data["vaksinasi"]["penambahan"]["jumlah_vaksinasi_1"],
        "new_vaccinated_2": data["vaksinasi"]["penambahan"]["jumlah_vaksinasi_2"],
    }