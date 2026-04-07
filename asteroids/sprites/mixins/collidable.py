"""Protocol for sprites that are drawable."""

from abc import ABC, abstractmethod
from typing import Self

from asteroids.sprites.base import BaseSprite
from pygame import Vector2


class Collidable(BaseSprite, ABC):
    """Protocol for sprites that are drawable."""

    position: Vector2
    radius: float

    @abstractmethod
    def collides_with(self, other: Self) -> bool:
        """Checks if the object collides with another object.

        Args:
            other: Another CircleShape object to check collision against
        Returns:
            True if the objects collide, False otherwise
        """
        ...
