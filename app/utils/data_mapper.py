def map_case_to_dict(case):
    return {
        "positive": case["jumlah_positif"]["value"],
        "recovered": case["jumlah_sembuh"]["value"],
        "deaths": case["jumlah_meninggal"]["value"],
        "active": case["jumlah_dirawat"]["value"]
    }

def map_vaccine_to_dict(vaccine):
    return {
        "vaccinated_1": vaccine["jumlah_vaksinasi_1"]["value"],
        "vaccinated_2": vaccine["jumlah_vaksinasi_2"]["value"]
    }

def sum_case_to_dict(cases):
    return {
        "positive": sum([case["jumlah_positif"]["value"] for case in cases]),
        "recovered": sum([case["jumlah_sembuh"]["value"] for case in cases]),
        "deaths": sum([case["jumlah_meninggal"]["value"] for case in cases]),
        
        # active cases still in doubt because of negative value
        "active": sum([case["jumlah_dirawat"]["value"] for case in cases if case["jumlah_dirawat"]["value"] > 0])
    }

def sum_vaccine_to_dict(vaccines):
    return {
        "vaccinated_1": sum([data["jumlah_vaksinasi_1"]["value"] for data in vaccines]),
        "vaccinated_2": sum([data["jumlah_vaksinasi_2"]["value"] for data in vaccines]),
    }

def map_year_month_tuple_to_str(year_month: tuple):
    return f"{year_month[0]}-{year_month[1]:02d}"
