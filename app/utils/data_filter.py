from datetime import datetime, timezone
from app.utils import key_parser, query_parser

def yearly_since(since: str, data):
    since_int = int(since)
    filtered_data = list(
        filter(
            lambda x: key_parser.parse_to_year_int(x["key"]) >= since_int,
            data 
        )
    )
    return filtered_data

def yearly_upto(upto: str, data):
    upto_int = int(upto)
    filtered_data = list(
        filter(
            lambda x: key_parser.parse_to_year_int(x["key"]) <= upto_int,
            data
        )
    )
    return filtered_data

def data_on_year(year: int, data):
    filtered_data = list(
        filter(
            lambda x: key_parser.parse_to_year_int(x["key"]) == year,
            data
        )
    )
    return filtered_data

def monthly_since(since: str, data):
    since_tuple = query_parser.parse_year_month_to_tuple(since)
        
    filtered_data = list(
        filter(
            lambda x: key_parser.parse_to_year_month_tuple(x["key"]) >= since_tuple,
            data
        )
    )

    return filtered_data

def monthly_upto(upto: str, data):
    upto_tuple = query_parser.parse_year_month_to_tuple(upto)
        
    filtered_data = list(
        filter(
            lambda x: key_parser.parse_to_year_month_tuple(x["key"]) <= upto_tuple,
            data 
        )
    )

    return filtered_data

def data_on_year_month(month: 'tuple[int, int]', data):
    filtered_data = list(
        filter(
            lambda x: key_parser.parse_to_year_month_tuple(x["key"]) == month,
            data
        )
    )
    return filtered_data

def data_on_month(month: int, data):
    filtered_data = list(
        filter(
            lambda x: key_parser.parse_to_month_int(x["key"]) == month,
            data
        )
    )
    return filtered_data

def daily_since(since: str, data):
    since_milliseconds = query_parser.parse_full_date_to_milliseconds(since)
    filtered_data = list(
        filter(
            lambda x: x["key"] >= since_milliseconds,
            data
        )
    )
    return filtered_data

def daily_upto(upto: str, data):
    upto_milliseconds = query_parser.parse_full_date_to_milliseconds(upto)
    filtered_data = list(
        filter(
            lambda x: x["key"] <= upto_milliseconds,
            data
        )
    )
    return filtered_data

def data_on_full_date(year: int, month: int, day: int, data):
    full_date_in_ms = int(datetime(year, month, day, tzinfo=timezone.utc).timestamp() * 1000)

    filtered_data = list(
        filter(
            lambda x: x["key"] == full_date_in_ms,
            data
        )
    )
    return filtered_data
