from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_welcome():
    response = client.get("/")
    assert response.status_code == 200


def test_generate():
    response = client.get("/generate")
    assert response.status_code == 200
    assert "token" in response.json()


def test_checksum():
    response = client.post(
        "/checksum",
        json={"text": "Hello World"}
    )

    assert response.status_code == 200
    assert "checksum" in response.json()