from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_get_daily():
    response = client.get("/daily")
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
    assert ("date" in data.keys()) == True
    assert type(data["date"]) == str

def test_get_daily_since_2021_01_01():
    response = client.get("/daily?since=2021.01.01")
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
    assert ("date" in data.keys()) == True
    assert type(data["date"]) == str

def test_get_daily_upto_2021_01_01():
    response = client.get("/daily?upto=2021.01.01")
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
    assert ("date" in data.keys()) == True
    assert type(data["date"]) == str

def test_get_daily_since_2021_01_02_upto_2021_01_03():
    response = client.get("/daily?since=2021.01.02&upto=2021.01.03")
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
    assert ("date" in data.keys()) == True
    assert type(data["date"]) == str

def test_get_daily_on_year_2021():
    response = client.get("/daily/2021")
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
    assert ("date" in data.keys()) == True
    assert type(data["date"]) == str

def test_get_daily_on_year_2021_since_2021_01_02():
    response = client.get("/daily/2021?since=2021.01.02")
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
    assert ("date" in data.keys()) == True
    assert type(data["date"]) == str

def test_get_daily_on_year_2021_upto_2021_01_02():
    response = client.get("/daily/2021?upto=2021.01.02")
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
    assert ("date" in data.keys()) == True
    assert type(data["date"]) == str

def test_get_daily_on_year_2021_since_2021_01_02_upto_2021_01_03():
    response = client.get("/daily/2021?since=2021.01.02&upto=2021.01.03")
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
    assert ("date" in data.keys()) == True
    assert type(data["date"]) == str

def test_get_daily_on_month_2021_01():
    response = client.get("/daily/2021/01")
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
    assert ("date" in data.keys()) == True
    assert type(data["date"]) == str

def test_get_daily_on_month_2021_01_since_2021_01_02():
    response = client.get("/daily/2021/01?since=2021.01.02")
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
    assert ("date" in data.keys()) == True
    assert type(data["date"]) == str

def test_get_daily_on_month_2021_01_upto_2021_01_02():
    response = client.get("/daily/2021/01?upto=2021.01.02")
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
    assert ("date" in data.keys()) == True
    assert type(data["date"]) == str

def test_get_daily_on_month_2021_01_since_2021_01_02_upto_2021_01_03():
    response = client.get("/daily/2021/01?since=2021.01.02&upto=2021.01.03")
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
    assert ("date" in data.keys()) == True
    assert type(data["date"]) == str

def test_get_daily_on_date_2021_01_01():
    response = client.get("/daily/2021/01/01")
    assert response.status_code == 200
    response_data = response.json()

    assert ("ok" in response_data.keys()) == True
    assert response_data["ok"] == True

    assert ("message" in response_data.keys()) == True
    assert response_data["message"] == "Data fetched successfully"

    assert ("data" in response_data.keys()) == True
    assert type(response_data["data"]) == dict
    
    data = response_data["data"]

    assert ("date" in data.keys()) == True
    assert type(data["date"]) == str
    assert data["date"] == "2021-01-01"
