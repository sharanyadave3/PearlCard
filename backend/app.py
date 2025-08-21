"""FastAPI application exposing the fare calculation service.

To run the server locally, install the dependencies from ``requirements.txt``
and execute the following command from within the ``backend`` directory:

```
uvicorn app:app --reload
```
"""

from typing import List

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .models import Journey, JourneyFare
from .services import FareRulesRepository, FareCalculator
from pathlib import Path


def create_app() -> FastAPI:
    """Factory for creating the FastAPI application instance."""
    app = FastAPI(
        title="PearlCard Fare Calculation API",
        description=(
            "Calculate metro fares for a list of journeys based on zone definitions. "
            "Post a JSON array of journey objects and receive individual fares "
            "along with the daily total."
        ),
        version="1.0.0",
    )

    # Instantiate repository and calculator
    repo = FareRulesRepository(json_path=str((Path(__file__).parent / "data" / "fares.json")))
    calculator = FareCalculator(repo)

    # Enable CORS so that a React frontend on another port can call this API
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # In production, restrict this to known hosts
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.post("/calculate-fares", response_model=dict)
    def calculate_fares(journeys: List[Journey]):
        """Calculate fares for a list of journeys.

        The payload must be a JSON array of objects with ``from_zone`` and
        ``to_zone`` fields.  Each object will be validated and converted into
        a ``Journey`` instance before processing.  The response contains
        the fare for each journey and the total daily fare.
        """
        try:
            results, total = calculator.calculate_journeys(journeys)
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc))
        return {"journeys": results, "total_fare": total}

    return app


# Create a global app instance for uvicorn
app = create_app()