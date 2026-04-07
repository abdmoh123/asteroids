"""Circle shape base class for asteroids - provided by boot.dev."""

from typing import override

from asteroids.sprites.base import BaseSprite
from asteroids.sprites.mixins.collidable import Collidable
from pygame.math import Vector2

type ColorValue = str | tuple[int, int, int]


class CircleShape(Collidable, BaseSprite):
    """Base class for game objects."""

    def __init__(self, x: float, y: float, radius: float) -> None:
        """Constructor for CircleShape."""
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.position: Vector2 = Vector2(x, y)
        self.velocity: Vector2 = Vector2(0, 0)
        self.radius: float = radius

    @override
    def collides_with(self, other: Collidable) -> bool:
        """Checks if the object collides with another object.

        Args:
            other: Another CircleShape object to check collision against
        Returns:
            True if the objects collide, False otherwise
        """
        distance_between: float = self.position.distance_to(other.position)
        return self.radius + other.radius > distance_between
