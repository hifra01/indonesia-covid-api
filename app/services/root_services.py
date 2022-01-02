from app.services.data_fetcher import total_and_update_cases, total_and_update_vaccines
async def fetch_total_and_update():
    case_data = await total_and_update_cases()
    vaccine_data = await total_and_update_vaccines()

    return {
        **case_data,
        **vaccine_data
    }