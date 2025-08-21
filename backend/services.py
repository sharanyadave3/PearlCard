"""Business logic for calculating fares.

This module encapsulates the fare rules and exposes high‑level operations to
compute the cost of one or more journeys.  By abstracting rules into a
repository class, additional data sources (e.g. databases) can be used in
future without changing the core logic.
"""

import json
from pathlib import Path
from typing import Dict, List, Tuple

from .models import Journey


class FareRulesRepository:


    def __init__(self, json_path: str) -> None:
        path = Path(json_path)
        if not path.exists():
            raise FileNotFoundError(f"Fare rules file not found: {json_path}")
        with path.open() as f:
            data = json.load(f)
        # normalise keys to ensure string mapping
        self._rules: Dict[str, float] = {str(k): float(v) for k, v in data.items()}

    def get_fare(self, from_zone: int, to_zone: int) -> float:

        key = f"{from_zone}-{to_zone}"
        if key in self._rules:
            return self._rules[key]
        rev_key = f"{to_zone}-{from_zone}"
        if rev_key in self._rules:
            return self._rules[rev_key]
        raise ValueError(f"No fare rule defined for zones {from_zone} and {to_zone}")


class FareCalculator:
    """Coordinates fare calculations for one or more journeys."""

    def __init__(self, repository: FareRulesRepository) -> None:
        self._repo = repository

    def calculate_journey_fare(self, journey: Journey) -> float:
        """Compute the fare for a single journey."""
        return self._repo.get_fare(journey.from_zone, journey.to_zone)

    def calculate_journeys(self, journeys: List[Journey]) -> Tuple[List[Dict[str, float]], float]:

        results: List[Dict[str, float]] = []
        total = 0.0
        for journey in journeys:
            fare = self.calculate_journey_fare(journey)
            results.append({
                "from_zone": journey.from_zone,
                "to_zone": journey.to_zone,
                "fare": fare,
            })
            total += fare
        return results, total