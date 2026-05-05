from fastapi.testclient import TestClient
from mock_agent import app
import os

client = TestClient(app)

def test_run_no_auth():
    # Make sure we don't accidentally pass if API_KEY is set in environment
    if "API_KEY" in os.environ:
        del os.environ["API_KEY"]
    response = client.post("/run", json={"agent": "test"})
    assert response.status_code == 403

def test_run_invalid_auth():
    os.environ["API_KEY"] = "secret"
    response = client.post("/run", json={"agent": "test"}, headers={"X-API-Key": "invalid"})
    assert response.status_code == 403

def test_run_valid_auth():
    os.environ["API_KEY"] = "secret"
    response = client.post("/run", json={"agent": "test"}, headers={"X-API-Key": "secret"})
    assert response.status_code == 200
    assert response.json()["agent"] == "test"
