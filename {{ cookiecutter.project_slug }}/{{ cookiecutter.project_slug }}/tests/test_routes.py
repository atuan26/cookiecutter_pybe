from fastapi.testclient import TestClient

from {{ cookiecutter.project_slug }}.main import app


client = TestClient(app)


def test_health():
    response = client.get("/v1/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}
