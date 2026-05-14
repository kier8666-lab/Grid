import sys
import asyncio
from unittest.mock import MagicMock

# --- INFRASTRUCTURE MOCKING ---
# In this environment, 'fastapi' and 'httpx' (required for TestClient) are not pre-installed.
# To ensure the test suite is runnable in this restricted environment while following
# standard patterns, we mock the 'fastapi' module before importing 'mock_agent'.

class MockTestClient:
    """
    A minimal mock of the FastAPI TestClient.
    It calls the 'run' handler directly while simulating the request environment.
    """
    def __init__(self, app):
        self.app = app

    def post(self, url, json=None):
        if url == "/run":
            # Direct call to the async handler
            # In a real TestClient, this would go through the FastAPI routing layer.
            class MockRequest:
                def __init__(self, data): self._data = data
                async def json(self): return self._data

            mock_req = MockRequest(json or {})
            response_data = asyncio.run(self.app.run(mock_req))

            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.json.return_value = response_data
            return mock_response
        raise ValueError(f"URL {url} not handled by MockTestClient")

# Mock fastapi BEFORE importing mock_agent
mock_fastapi = MagicMock()
# Use a simple decorator that returns the function unchanged
mock_fastapi.FastAPI.return_value.post = lambda *args, **kwargs: lambda f: f
sys.modules["fastapi"] = mock_fastapi

# Now we can safely import the application
import mock_agent

# --- TESTS ---

def test_run_endpoint_happy_path():
    """
    Verifies that /run endpoint processes a standard payload correctly.
    """
    client = MockTestClient(mock_agent)
    payload = {
        "agent": "PV-Optimizer",
        "trace_id": "DL-test-123",
        "payload": {"param": 1}
    }

    response = client.post("/run", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["agent"] == "PV-Optimizer"
    assert data["trace_id"] == "DL-test-123"
    assert data["status"] == "OK"
    assert data["ts"].endswith("Z")

def test_run_endpoint_defaults():
    """
    Verifies that /run endpoint uses default values when payload is empty.
    """
    client = MockTestClient(mock_agent)

    response = client.post("/run", json={})

    assert response.status_code == 200
    data = response.json()
    assert data["agent"] == "unknown"
    assert data["trace_id"] == "DL-local"
    assert data["status"] == "OK"
