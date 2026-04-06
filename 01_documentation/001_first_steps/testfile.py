"""
Fermion evaluation tests for FastAPI First Steps lab.
Tests use HTTPX's TestClient to call routes without a running server.
"""
import os
import sys
import importlib

import pytest
from fastapi.testclient import TestClient

# Make the student's code directory importable
USER_CODE_DIR = os.environ.get("USER_CODE_DIR", "/home/damner/code")
sys.path.insert(0, USER_CODE_DIR)


@pytest.fixture(scope="module")
def client():
    """Import student's app and wrap it in a TestClient."""
    main = importlib.import_module("main")
    assert hasattr(main, "app"), (
        "No `app` variable found in main.py. "
        "Make sure you created a FastAPI instance called `app`."
    )
    return TestClient(main.app)


def test_root_returns_status_ok(client):
    """GET / should return {\"hello\": \"world\"}."""
    response = client.get("/")
    data = response.json()
    assert data.get("hello") == "world", (
        f"Expected {{\"hello\": \"world\"}}, got {data}"
    )
