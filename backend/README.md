# PearlCard Backend

This directory contains the implementation of the PearlCard fare calculation API.

The service is built with [FastAPI](https://fastapi.tiangolo.com/) and exposes a
single endpoint that computes fares for a list of daily journeys.  Fare rules
are defined externally in a JSON file (`data/fares.json`) so they can be
updated or extended without changing any code.  The design follows object‑
oriented principles to ensure the logic is modular, testable and easy to
extend.

## Requirements

* Python 3.9 or higher
* pip package manager

## Installation

Navigate into the `backend` folder and install the dependencies listed in
`requirements.txt`:

```bash
cd backend
python -m venv venv  # optional
source venv/bin/activate
pip install -r requirements.txt
```

## Running the Server

To start the development server, run:

```bash
uvicorn app:app --reload
```

The API will be available at <http://localhost:8000>. Interactive
documentation is automatically generated and can be accessed at
<http://localhost:8000/docs>.

## API Usage

### `POST /calculate-fares`

Calculate the fare for one or more journeys.

**Request Body**: an array of objects, each containing `from_zone` and
`to_zone` integers. Up to 20 journeys may be submitted at once.

Example request:

```json
[
  {"from_zone": 1, "to_zone": 1},
  {"from_zone": 2, "to_zone": 3}
]
```

**Response**: a JSON object with a `journeys` array (each element
containing the zones and the calculated `fare`) and a `total_fare` number
representing the sum of all fares.

Example response:

```json
{
  "journeys": [
    {"from_zone": 1, "to_zone": 1, "fare": 40},
    {"from_zone": 2, "to_zone": 3, "fare": 45}
  ],
  "total_fare": 85
}
```

## Testing

Unit tests are located in the `tests` folder and can be run with
[pytest](https://docs.pytest.org/):

```bash
pip install -r requirements.txt
pip install pytest
pytest
```

The tests use FastAPI's `TestClient` to simulate HTTP requests against the
running application. Additional tests can be added to cover more scenarios as
needed.