

from dataclasses import dataclass


@dataclass
class Journey:
    """Represents a single commuter journey between two zones."""
    from_zone: int
    to_zone: int