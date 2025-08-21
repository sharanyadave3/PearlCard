"""Unit tests for the PearlCard API.

These tests exercise the REST endpoint directly using FastAPI's TestClient.  To
run the tests, execute ``pytest`` from the ``backend`` directory.
"""

from fastapi.testclient import TestClient

from backend.app import create_app


# Use a fresh app instance for each test to avoid state leakage
client = TestClient(create_app())


def test_calculate_fares_success():
    """Verify that the API returns correct fares and totals for valid journeys."""
    journeys = [
        {"from_zone": 1, "to_zone": 1},  # expected 40
        {"from_zone": 1, "to_zone": 2},  # expected 55
        {"from_zone": 3, "to_zone": 2},  # expected 45 (reverse mapping)
    ]
    response = client.post("/calculate-fares", json=journeys)
    assert response.status_code == 200
    data = response.json()
    assert "journeys" in data
    assert "total_fare" in data
    fares = [j["fare"] for j in data["journeys"]]
    assert fares == [40, 55, 45]
    assert data["total_fare"] == sum(fares)


def test_calculate_fares_invalid_zones():
    """Ensure the API returns a 400 error for journeys without defined fares."""
    invalid_journey = [{"from_zone": 4, "to_zone": 5}]
    response = client.post("/calculate-fares", json=invalid_journey)
    assert response.status_code == 400
    assert "detail" in response.json()