from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_read_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"ok": "home"}


def test_read_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"ok": "health"}
