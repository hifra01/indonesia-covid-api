from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_get_yearly():
    response = client.get("/yearly")
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
    assert ("year" in data.keys()) == True

def test_get_yearly_since_2021():
    response = client.get("/yearly?since=2021")
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
    assert ("year" in data.keys()) == True

def test_get_yearly_upto_2021():
    response = client.get("/yearly?upto=2021")
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
    assert ("year" in data.keys()) == True

def test_get_yearly_since_2020_upto_2021():
    response = client.get("/yearly?since=2020&upto=2021")
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
    assert ("year" in data.keys()) == True

def test_get_yearly_on_2021():
    response = client.get("/yearly/2021")
    assert response.status_code == 200
    response_data = response.json()

    assert ("ok" in response_data.keys()) == True
    assert response_data["ok"] == True

    assert ("message" in response_data.keys()) == True
    assert response_data["message"] == "Data fetched successfully"

    assert ("data" in response_data.keys()) == True
    assert type(response_data["data"]) == dict
    
    data = response_data["data"]

    assert ("year" in data.keys()) == True
    assert type(data["year"]) == str
    assert data["year"] == "2021"
