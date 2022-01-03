from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_get_monthly():
    response = client.get("/monthly")
    assert response.status_code == 200
    response_data = response.json()

    assert ("ok" in response_data.keys()) == True
    assert response_data["ok"] == True

    assert ("message" in response_data.keys()) == True
    assert response_data["message"] == "Data fetched successfully"

    assert ("data" in response_data.keys()) == True
    assert type(response_data["data"]) == list
    assert len(response_data["data"]) > 0

    data = response_data["data"][0]
    assert type(data) == dict
    assert ("month" in data.keys()) == True

def test_get_monthly_since_2021_01():
    response = client.get("/monthly?since=2020.01")
    assert response.status_code == 200
    response_data = response.json()

    assert ("ok" in response_data.keys()) == True
    assert response_data["ok"] == True

    assert ("message" in response_data.keys()) == True
    assert response_data["message"] == "Data fetched successfully"

    assert ("data" in response_data.keys()) == True
    assert type(response_data["data"]) == list
    assert len(response_data["data"]) > 0

    data = response_data["data"][0]
    assert type(data) == dict
    assert ("month" in data.keys()) == True

def test_get_monthly_upto_2021_01():
    response = client.get("/monthly?upto=2021.01")
    assert response.status_code == 200
    response_data = response.json()

    assert ("ok" in response_data.keys()) == True
    assert response_data["ok"] == True

    assert ("message" in response_data.keys()) == True
    assert response_data["message"] == "Data fetched successfully"

    assert ("data" in response_data.keys()) == True
    assert type(response_data["data"]) == list
    assert len(response_data["data"]) > 0

    data = response_data["data"][0]
    assert type(data) == dict
    assert ("month" in data.keys()) == True

def test_get_monthly_since_2021_01_upto_2021_02():
    response = client.get("/monthly?since=2021.01&upto=2021.02")
    assert response.status_code == 200
    response_data = response.json()

    assert ("ok" in response_data.keys()) == True
    assert response_data["ok"] == True

    assert ("message" in response_data.keys()) == True
    assert response_data["message"] == "Data fetched successfully"

    assert ("data" in response_data.keys()) == True
    assert type(response_data["data"]) == list
    assert len(response_data["data"]) > 0
    assert len(response_data["data"]) == 2

    data = response_data["data"][0]
    assert type(data) == dict
    assert ("month" in data.keys()) == True

def test_get_monthly_on_year_2021():
    response = client.get("/monthly/2021")
    assert response.status_code == 200
    response_data = response.json()

    assert ("ok" in response_data.keys()) == True
    assert response_data["ok"] == True

    assert ("message" in response_data.keys()) == True
    assert response_data["message"] == "Data fetched successfully"

    assert ("data" in response_data.keys()) == True
    assert type(response_data["data"]) == list
    assert len(response_data["data"]) > 0

    data = response_data["data"][0]
    assert type(data) == dict
    assert ("month" in data.keys()) == True

def test_get_monthly_on_year_2021_since_2021_02():
    response = client.get("/monthly/2021?since=2021.02")
    assert response.status_code == 200
    response_data = response.json()

    assert ("ok" in response_data.keys()) == True
    assert response_data["ok"] == True

    assert ("message" in response_data.keys()) == True
    assert response_data["message"] == "Data fetched successfully"

    assert ("data" in response_data.keys()) == True
    assert type(response_data["data"]) == list
    assert len(response_data["data"]) > 0
    assert len(response_data["data"]) == 11

    data = response_data["data"][0]
    assert type(data) == dict
    assert ("month" in data.keys()) == True

def test_get_monthly_on_year_2021_upto_2021_02():
    response = client.get("/monthly/2021?upto=2021.02")
    assert response.status_code == 200
    response_data = response.json()

    assert ("ok" in response_data.keys()) == True
    assert response_data["ok"] == True

    assert ("message" in response_data.keys()) == True
    assert response_data["message"] == "Data fetched successfully"

    assert ("data" in response_data.keys()) == True
    assert type(response_data["data"]) == list
    assert len(response_data["data"]) > 0
    assert len(response_data["data"]) == 2

    data = response_data["data"][0]
    assert type(data) == dict
    assert ("month" in data.keys()) == True

def test_get_monthly_on_year_2021_since_2021_01_upto_2021_02():
    response = client.get("/monthly/2021?since=2021.01&upto=2021.02")
    assert response.status_code == 200
    response_data = response.json()

    assert ("ok" in response_data.keys()) == True
    assert response_data["ok"] == True

    assert ("message" in response_data.keys()) == True
    assert response_data["message"] == "Data fetched successfully"

    assert ("data" in response_data.keys()) == True
    assert type(response_data["data"]) == list
    assert len(response_data["data"]) > 0
    assert len(response_data["data"]) == 2

    data = response_data["data"][0]
    assert type(data) == dict
    assert ("month" in data.keys()) == True

def test_get_monthly_on_month_2021_01():
    response = client.get("/monthly/2021/01")
    assert response.status_code == 200
    response_data = response.json()

    assert ("ok" in response_data.keys()) == True
    assert response_data["ok"] == True

    assert ("message" in response_data.keys()) == True
    assert response_data["message"] == "Data fetched successfully"

    assert ("data" in response_data.keys()) == True
    assert type(response_data["data"]) == dict
    
    data = response_data["data"]

    assert ("month" in data.keys()) == True
    assert type(data["month"]) == str
    assert data["month"] == "2021-01"
