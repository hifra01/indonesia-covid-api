from datetime import datetime

def parse_year(key: int):
    timestamp = key/1000
    return datetime.utcfromtimestamp(timestamp).year