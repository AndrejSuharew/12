from unittest.mock import patch

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_endpoint() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "running"


@patch("app.main.check_db_connection", return_value=True)
def test_health_check_success(mock_db: object) -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "database": "connected"}


@patch("app.main.check_db_connection", return_value=False)
def test_health_check_db_down(mock_db: object) -> None:
    response = client.get("/health")
    assert response.status_code == 503
