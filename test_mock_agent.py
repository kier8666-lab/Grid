import sys
from unittest.mock import MagicMock

# -------------------------------------------------------------------------
# Framework Mocking Section
# -------------------------------------------------------------------------
# Since we cannot install dependencies (no internet), we must mock the
# framework to allow the code to be imported and unit-tested.
# While the review suggested TestClient, it is unavailable without httpx
# and starlette/fastapi installed. We provide the minimal surface for
# mock_agent.py to function.

class MockRequest:
    def __init__(self, json_data):
        self._json_data = json_data
    async def json(self):
        return self._json_data

mock_fastapi = MagicMock()
mock_app = MagicMock()
mock_fastapi.FastAPI.return_value = mock_app

# The decorator @app.post("/run") must return the function it decorates.
def mock_post_decorator(path):
    def wrapper(f):
        return f
    return wrapper

mock_app.post.side_effect = mock_post_decorator

sys.modules["fastapi"] = mock_fastapi

# -------------------------------------------------------------------------
# Tests Section
# -------------------------------------------------------------------------
import unittest
import asyncio
import datetime
from mock_agent import run

class TestMockAgent(unittest.TestCase):
    def setUp(self):
        # We use a fresh loop for each test to ensure determinism
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

    def tearDown(self):
        self.loop.close()

    def test_run_endpoint_success(self):
        """Tests the /run endpoint with a valid payload."""
        payload = {"agent": "PV-Optimizer", "trace_id": "trace-123"}
        request = MockRequest(payload)

        response = self.loop.run_until_complete(run(request))

        self.assertEqual(response["agent"], "PV-Optimizer")
        self.assertEqual(response["trace_id"], "trace-123")
        self.assertEqual(response["status"], "OK")
        self.assertIn("ts", response)

        # Verify timestamp format
        ts = response["ts"]
        if ts.endswith("Z"):
            ts = ts[:-1] + "+00:00"
        datetime.datetime.fromisoformat(ts)

    def test_run_endpoint_defaults(self):
        """Tests that the endpoint uses correct defaults for missing fields."""
        payload = {}
        request = MockRequest(payload)

        response = self.loop.run_until_complete(run(request))

        self.assertEqual(response["agent"], "unknown")
        self.assertEqual(response["trace_id"], "DL-local")
        self.assertEqual(response["status"], "OK")

if __name__ == "__main__":
    unittest.main()
