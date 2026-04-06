"""Circle shape base class for asteroids - provided by boot.dev."""

from typing import Self

import pygame
from pygame.math import Vector2
from pygame.surface import Surface

type ColorValue = str | tuple[int, int, int]


class CircleShape(pygame.sprite.Sprite):
    """Base class for game objects."""

    def __init__(self, x: float, y: float, radius: float) -> None:
        """Constructor for CircleShape."""
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)  # pyright: ignore[reportUnknownMemberType, reportUnknownArgumentType, reportAttributeAccessIssue]
        else:
            super().__init__()

        self.position: Vector2 = Vector2(x, y)
        self.velocity: Vector2 = Vector2(0, 0)
        self.radius: float = radius

    def draw(self, screen: Surface) -> None:
        """Draws the object to the screen."""
        raise NotImplementedError()

    def update(self, dt: float) -> None:
        """Updates the object."""
        raise NotImplementedError()

    def collides_with(self, other: Self) -> bool:
        """Checks if the object collides with another object.

        Args:
            other: Another CircleShape object to check collision against
        Returns:
            True if the objects collide, False otherwise
        """
        distance_between: float = self.position.distance_to(other.position)
        return self.radius + other.radius > distance_between
