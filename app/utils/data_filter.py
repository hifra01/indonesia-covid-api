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