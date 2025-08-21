# PearlCard Backend

This directory contains the implementation of the PearlCard fare calculation API.

The service is built with **Flask** to ensure compatibility with Python 3.13 and
exposes a single endpoint that computes fares for a list of daily journeys.  Fare
rules are defined externally in a JSON file (`data/fares.json`) so they can be
updated or extended without changing any code.  The design follows object‑
oriented principles to ensure the logic is modular, testable and easy to extend.

## Requirements

* Python 3.13 (or any modern Python 3.x)
* pip package manager

## Installation

Navigate into the `backend` folder and install the dependencies listed in
`requirements.txt`:

```bash
cd backend
python -m venv venv  # optional
source venv/bin/activate  # venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Running the Server

To start the development server, run:

```bash
python -m backend.app
```

By default the application listens on <http://localhost:8000>. You can set
a custom port by defining the `PORT` environment variable before running the
script.

## API Usage

### `POST /calculate-fares`

Calculate the fare for one or more journeys.

**Request body**: JSON array of objects, each containing `from_zone` and
`to_zone` integers. Up to 20 journeys may be submitted at once.

**Response**: a JSON object with a `journeys` array (each element containing
the zones and the calculated `fare`) and a `total_fare` number representing
the sum of all fares.  If any zone pair does not exist in the rules, or if
the input is malformed, the API returns an error message with a `400` status.

## Testing

Unit tests are located in the `tests` folder and can be run with
[pytest](https://docs.pytest.org/):

```bash
pip install -r requirements.txt
pytest
```

The tests use Flask’s test client to simulate HTTP requests against the
running application. Additional tests can be added to cover more scenarios as
needed.