from fastapi import HTTPException
from app.services.data_fetcher import daily_cases, daily_vaccines
from app.utils import key_parser
from app.utils.data_mapper import sum_case_to_dict, sum_vaccine_to_dict

async def fetch_yearly(since, upto):
    case_data = await daily_cases()
    vaccine_data = await daily_vaccines()

    if since is not None:
        since_int = int(since)
        case_data = list(
            filter(
                lambda data: key_parser.parse_to_year_int(data["key"]) >= since_int,
                case_data 
            )
        )

        vaccine_data = list(
            filter(
                lambda data: key_parser.parse_to_year_int(data["key"]) >= since_int,
                vaccine_data 
            )
        )

    if upto is not None:
        upto_int = int(upto)
        case_data = list(
            filter(
                lambda data: key_parser.parse_to_year_int(data["key"]) <= upto_int,
                case_data 
            )
        )

        vaccine_data = list(
            filter(
                lambda data: key_parser.parse_to_year_int(data["key"]) <= upto_int,
                vaccine_data 
            )
        )

    yearly_data = []

    years = sorted(set(map(lambda data: key_parser.parse_to_year_int(data["key"]), case_data)))

    for year in years:
        cases_on_year = list(
            filter(
                lambda data: key_parser.parse_to_year_int(data["key"]) == year,
                case_data
            )
        )
        mapped_case = sum_case_to_dict(cases_on_year)
        mapped_vaccine = dict()

        vaccine_on_year = list(
            filter(
                lambda data: key_parser.parse_to_year_int(data["key"]) == year,
                vaccine_data
            )
        )

        if len(vaccine_on_year) > 0:
            mapped_vaccine = sum_vaccine_to_dict(vaccine_on_year)

        yearly_data.append({
            "year": str(year),
            **mapped_case,
            **mapped_vaccine
        })
    
    return yearly_data

async def fetch_yearly_on_year(year):
    case_data = await daily_cases()
    vaccine_data = await daily_vaccines()

    year_int = int(year)
    
    cases_on_year = list(
        filter(
            lambda data: key_parser.parse_to_year_int(data["key"]) == year_int,
            case_data
        )
    )

    if len(cases_on_year) == 0:
        raise HTTPException(status_code=404, detail="Data not found")

    vaccine_on_year = list(
        filter(
            lambda data: key_parser.parse_to_year_int(data["key"]) == year,
            vaccine_data
        )
    )

    mapped_case = sum_case_to_dict(cases_on_year)
    mapped_vaccine = dict()

    if len(vaccine_on_year) > 0:
        mapped_vaccine = sum_vaccine_to_dict(vaccine_on_year)

    return {
        "year": year,
        **mapped_case,
        **mapped_vaccine
    }
    