import aiohttp
from app.services.data_fetcher import daily_cases, daily_vaccines
from app.utils.data_mapper import map_case_to_dict, map_vaccine_to_dict
from app.utils.key_parser import parse_to_full_date_str
from app.utils.query_parser import parse_full_date_to_milliseconds

async def fetch_daily(since, upto):
    case_data = await daily_cases()
    vaccine_data = await daily_vaccines()

    if since is not None:
        since_milliseconds = parse_full_date_to_milliseconds(since)
        case_data = list(
            filter(
                lambda data: data["key"] >= since_milliseconds,
                case_data
            )
        )
        
        vaccine_data = list(
            filter(
                lambda data: data["key"] >= since_milliseconds,
                vaccine_data
            )
        )

    if upto is not None:
        upto_milliseconds = parse_full_date_to_milliseconds(upto)
        case_data = list(
            filter(
                lambda data: data["key"] <= upto_milliseconds,
                case_data
            )
        )

        vaccine_data = list(
            filter(
                lambda data: data["key"] <= upto_milliseconds,
                vaccine_data
            )
        )

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

