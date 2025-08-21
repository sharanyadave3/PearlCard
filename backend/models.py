"""Data models used throughout the PearlCard backend.

These Pydantic models define the shape of incoming and outgoing data.  Using
Pydantic ensures type validation and serialization happen consistently at the
framework boundary.
"""

from pydantic import BaseModel, Field


class Journey(BaseModel):
    """Represents a single commuter journey between two zones."""

    from_zone: int = Field(..., gt=0, description="Starting zone for the journey")
    to_zone: int = Field(..., gt=0, description="Destination zone for the journey")


class JourneyFare(BaseModel):
    """Extends ``Journey`` with a calculated fare."""

    from_zone: int
    to_zone: int
    fare: float