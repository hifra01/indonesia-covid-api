from datetime import datetime

def parse_to_year_int(key: int):
    timestamp = key/1000
    return datetime.utcfromtimestamp(timestamp).year

def parse_to_month_int(key: int):
    timestamp = key/1000
    return datetime.utcfromtimestamp(timestamp).month

def parse_to_day_int(key: int):
    timestamp = key/1000
    return datetime.utcfromtimestamp(timestamp).day

def parse_to_full_date_str(key: int):
    year = parse_to_year_int(key)
    month = parse_to_month_int(key)
    day = parse_to_day_int(key)

    full_date = f"{year}-{month:02d}-{day:02d}"

    return full_date

# Used for date value in monthly endpoint
def parse_to_year_month_str(key: int):
    year = parse_to_year_int(key)
    month = parse_to_month_int(key)

    year_month = f"{year}-{month:02d}"

    return year_month

# Used to compare year and month of data
def parse_to_year_month_tuple(key: int):
    year = parse_to_year_int(key)
    month = parse_to_month_int(key)

    year_month = (year, month)

    return year_month
