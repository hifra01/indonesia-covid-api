from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_get_root():
    response = client.get("/")
    assert response.status_code == 200
    response_data = response.json()

    assert ("ok" in response_data.keys()) == True
    assert response_data["ok"] == True

    assert ("message" in response_data.keys()) == True
    assert response_data["message"] == "Data fetched successfully"

    assert ("data" in response_data.keys()) == True
    assert type(response_data["data"]) == dict

    data = response_data["data"]

    assert ("total_positive" in data.keys()) == True
    assert type(data["total_positive"]) == int

    assert ("total_recovered" in data.keys()) == True
    assert type(data["total_recovered"]) == int

    assert ("total_deaths" in data.keys()) == True
    assert type(data["total_deaths"]) == int

    assert ("total_active" in data.keys()) == True
    assert type(data["total_active"]) == int

    assert ("new_positive" in data.keys()) == True
    assert type(data["new_positive"]) == int

    assert ("new_recovered" in data.keys()) == True
    assert type(data["new_recovered"]) == int

    assert ("new_deaths" in data.keys()) == True
    assert type(data["new_deaths"]) == int

    assert ("new_active" in data.keys()) == True
    assert type(data["new_active"]) == int

    assert ("total_vaccinated_1" in data.keys()) == True
    assert type(data["total_vaccinated_1"]) == int

    assert ("total_vaccinated_2" in data.keys()) == True
    assert type(data["total_vaccinated_2"]) == int

    assert ("new_vaccinated_1" in data.keys()) == True
    assert type(data["new_vaccinated_1"]) == int

    assert ("new_vaccinated_2" in data.keys()) == True
    assert type(data["new_vaccinated_2"]) == int
    