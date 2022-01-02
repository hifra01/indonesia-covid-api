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