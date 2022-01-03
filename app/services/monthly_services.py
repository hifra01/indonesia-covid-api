from fastapi import HTTPException
from app.services.data_fetcher import daily_cases, daily_vaccines
from app.utils import query_parser, key_parser, data_filter
from app.utils.data_mapper import sum_case_to_dict, sum_vaccine_to_dict, map_year_month_tuple_to_str

async def fetch_monthly(since, upto):
    case_data = await daily_cases()
    vaccine_data = await daily_vaccines()

    if since is not None:       
        case_data = data_filter.monthly_since(since, case_data)
        vaccine_data = data_filter.monthly_since(since, vaccine_data)

    if upto is not None:     
        case_data = data_filter.monthly_upto(upto, case_data)
        vaccine_data = data_filter.monthly_upto(upto, vaccine_data)

    monthly_data = []

    months = sorted(
        set(
            map(
                lambda data: key_parser.parse_to_year_month_tuple(data["key"]),
                case_data
            )
        )
    )

    for month in months:
        cases_on_month = data_filter.data_on_year_month(month, case_data)
        vaccine_on_month = data_filter.data_on_year_month(month, vaccine_data)

        mapped_case = sum_case_to_dict(cases_on_month)
        mapped_vaccine = dict()

        if len(vaccine_on_month) > 0:
            mapped_vaccine = sum_vaccine_to_dict(vaccine_on_month)

        monthly_data.append({
            "month": map_year_month_tuple_to_str(month),
            **mapped_case,
            **mapped_vaccine
        })
    
    return monthly_data

async def fetch_monthly_on_year(year, since, upto):
    case_data = await daily_cases()
    vaccine_data = await daily_vaccines()

    year_int = int(year)

    case_data = data_filter.data_on_year(year_int, case_data)
    vaccine_data = data_filter.data_on_year(year_int, vaccine_data)

    if since is not None:       
        case_data = data_filter.monthly_since(since, case_data)
        vaccine_data = data_filter.monthly_since(since, vaccine_data)

    if upto is not None:     
        case_data = data_filter.monthly_upto(upto, case_data)
        vaccine_data = data_filter.monthly_upto(upto, vaccine_data)

    months = sorted(
        set(
            map(
                lambda data: key_parser.parse_to_year_month_tuple(data["key"]),
                case_data
            )
        )
    )

    monthly_data = []

    for month in months:
        cases_on_month = data_filter.data_on_year_month(month, case_data)
        vaccine_on_month = data_filter.data_on_year_month(month, vaccine_data)

        mapped_case = sum_case_to_dict(cases_on_month)
        mapped_vaccine = dict()

        if len(vaccine_on_month) > 0:
            mapped_vaccine = sum_vaccine_to_dict(vaccine_on_month)

        monthly_data.append({
            "month": map_year_month_tuple_to_str(month),
            **mapped_case,
            **mapped_vaccine
        })
    
    return monthly_data

async def fetch_monthly_on_month(year, month):
    case_data = await daily_cases()
    vaccine_data = await daily_vaccines()

    year_int = int(year)
    month_int = int(month)

    case_data = data_filter.data_on_year(year_int, case_data)
    vaccine_data = data_filter.data_on_year(year_int, vaccine_data)

    case_data = data_filter.data_on_month(month_int, case_data)
    vaccine_data = data_filter.data_on_month(month_int, vaccine_data)

    if len(case_data) == 0:
        raise HTTPException(status_code=404, detail="Data not found")

    mapped_case = sum_case_to_dict(case_data)
    mapped_vaccine = dict()

    if len(vaccine_data) > 0:
        mapped_vaccine = sum_vaccine_to_dict(vaccine_data)

    return {
        "month": map_year_month_tuple_to_str((year_int, month_int)),
        **mapped_case,
        **mapped_vaccine
    }
