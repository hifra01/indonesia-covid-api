from datetime import datetime,  timezone

def parse_full_date_to_milliseconds(date: str):
    date_splitted = date.split(".")
    year = int(date_splitted[0])
    month = int(date_splitted[1])
    day = int(date_splitted[2])

    new_date = datetime(year, month, day, tzinfo=timezone.utc)

    milliseconds = new_date.timestamp() * 1000

    return milliseconds
