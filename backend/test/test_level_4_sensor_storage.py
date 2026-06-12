from fastapi.testclient import TestClient

from conftest import get_fastapi_app


def test_level_4_post_api_sensors_menyimpan_data_terbaru():
    client = TestClient(get_fastapi_app())
    payload = {
        "temperature": 28,
        "humidity": 63,
        "moisture": 41,
    }

    create_response = client.post("/api/sensors", json=payload)

    assert create_response.status_code == 201
    assert create_response.json() == payload

    latest_response = client.get("/api/sensors")

    assert latest_response.status_code == 200
    assert latest_response.json() == payload
