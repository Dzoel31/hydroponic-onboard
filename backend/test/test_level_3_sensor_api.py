from fastapi.testclient import TestClient

from conftest import get_fastapi_app


def test_level_3_get_api_sensors_mengembalikan_data_sensor():
    client = TestClient(get_fastapi_app())

    response = client.get("/api/sensors")

    assert response.status_code == 200

    body = response.json()
    assert "temperature" in body
    assert "humidity" in body
    assert "moisture" in body

    assert isinstance(body["temperature"], (int, float))
    assert isinstance(body["humidity"], (int, float))
    assert isinstance(body["moisture"], int)
