
from backend.app import create_app


def _create_client():
    """Helper to create a new Flask test client for each test."""
    app = create_app()
    app.testing = True
    return app.test_client()


def test_calculate_fares_success():
    """Verify that the API returns correct fares and totals for valid journeys."""
    client = _create_client()
    journeys = [
        {"from_zone": 1, "to_zone": 1},  # expected 40
        {"from_zone": 1, "to_zone": 2},  # expected 55
        {"from_zone": 3, "to_zone": 2},  # expected 45 (reverse mapping)
    ]
    response = client.post("/calculate-fares", json=journeys)
    assert response.status_code == 200
    data = response.get_json()
    assert "journeys" in data
    assert "total_fare" in data
    fares = [j["fare"] for j in data["journeys"]]
    assert fares == [40, 55, 45]
    assert data["total_fare"] == sum(fares)


def test_calculate_fares_invalid_zones():
    """Ensure the API returns a 400 error for journeys without defined fares."""
    client = _create_client()
    invalid_journey = [{"from_zone": 4, "to_zone": 5}]
    response = client.post("/calculate-fares", json=invalid_journey)
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data