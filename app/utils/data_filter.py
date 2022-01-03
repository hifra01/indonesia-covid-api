from app.utils import key_parser

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