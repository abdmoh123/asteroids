"""Protocol for sprites that are updatable."""

from abc import ABC, abstractmethod
from typing import override

from asteroids.sprites.base import BaseSprite


class Updatable(BaseSprite, ABC):
    """Protocol for sprites that are updatable."""

    @abstractmethod
    @override
    def update(self, dt: float) -> None:
        """Performs some update on a given sprite."""
        ...
