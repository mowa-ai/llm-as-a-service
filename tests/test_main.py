import pytest
from fastapi.testclient import TestClient

from laas.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}


@pytest.mark.slow
def test_process_message():
    json_request = {
        "history": [
            {
                "role": "system",
                "content": "You are a nice assistant. Start each sentence with Hue hue",
            },
            {"role": "user", "content": "How are you"},
        ]
    }
    with TestClient(app) as client:
        response = client.post("/process_message", json=json_request)
        assert response.status_code == 200
        assert response.json()[:7] == "Hue hue"
