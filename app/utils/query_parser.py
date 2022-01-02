from datetime import datetime, timezone

def parse_full_date_to_milliseconds(date: str):
    date_splitted = date.split(".")
    year = int(date_splitted[0])
    month = int(date_splitted[1])
    day = int(date_splitted[2])

    new_date = datetime(year, month, day, tzinfo=timezone.utc)

    milliseconds = new_date.timestamp() * 1000

    return milliseconds

def parse_year_month_to_tuple(year_month):
    year_month_splitted = year_month.split(".")
    year = int(year_month_splitted[0])
    month = int(year_month_splitted[1])

    return (year, month)