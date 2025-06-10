from fastapi.testclient import TestClient
from flight_api import app

client = TestClient(app)

def test_create_and_get_flight():
    response = client.post(
        "/flights",
        json={"origin": "NYC", "destination": "LAX", "departure_time": "2024-01-01T10:00"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    flight_id = data["id"]

    get_resp = client.get(f"/flights/{flight_id}")
    assert get_resp.status_code == 200
    assert get_resp.json()["origin"] == "NYC"


def test_create_reservation():
    client.post(
        "/flights",
        json={"origin": "PAR", "destination": "LON", "departure_time": "2024-02-01T09:00"},
    )
    res_resp = client.post(
        "/reservations",
        json={"flight_id": 2, "passenger_name": "John"},
    )
    assert res_resp.status_code == 200
    res_data = res_resp.json()
    assert res_data["flight_id"] == 2
    assert res_data["passenger_name"] == "John"
