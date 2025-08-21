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
    """Loads and provides access to zone‑based fare rules.

    The rules are defined in a simple JSON structure where keys are
    ``"<from>-<to>"`` strings and values are numeric fares.  When a pair is
    requested, the repository will also attempt to reverse the key if the
    direct mapping isn't present.
    """

    def __init__(self, json_path: str) -> None:
        path = Path(json_path)
        if not path.exists():
            raise FileNotFoundError(f"Fare rules file not found: {json_path}")
        with path.open() as f:
            data = json.load(f)
        # normalise keys to ensure string mapping
        self._rules: Dict[str, float] = {str(k): float(v) for k, v in data.items()}

    def get_fare(self, from_zone: int, to_zone: int) -> float:
        """Return the fare for a single trip between ``from_zone`` and ``to_zone``.

        If no explicit rule exists for the pair, the method will attempt
        to look up the reversed pair.  If still not found, a ``ValueError``
        will be raised.
        """
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
        """Return individual fares and the aggregate total for a list of journeys.

        Parameters
        ----------
        journeys:
            A list of ``Journey`` objects representing a commuter's daily trips.

        Returns
        -------
        Tuple[List[Dict[str, float]], float]
            A tuple containing a list of dictionaries (each with from_zone,
            to_zone, fare) and a numeric total of all fares.
        """
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