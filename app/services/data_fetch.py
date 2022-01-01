import aiohttp
from app.configs import datasource

async def __get_case_data(session: aiohttp.ClientSession):
    async with session.get(datasource.case_update_url) as response:
        data = await response.json()
    return data

async def __get_vaccine_data(session: aiohttp.ClientSession):
    async with session.get(datasource.vaccine_update_url) as response:
        data = await response.json()
    return data

async def getTotalData():
    
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
