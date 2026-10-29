"""Tests de démarrage du mini-projet (semaine 1)."""
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_returns_200() -> None:
    response = client.get("/health")
    assert response.status_code == 200


def test_health_returns_expected_payload() -> None:
    response = client.get("/health")
    assert response.json() == {"status": "ok"}


def test_unknown_endpoint_returns_404() -> None:
    response = client.get("/not-an-endpoint")
    assert response.status_code == 404
