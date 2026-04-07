"""Protocol for sprites that are drawable."""

from abc import ABC, abstractmethod

from asteroids.sprites.base import BaseSprite
from pygame import Surface


class Drawable(BaseSprite, ABC):
    """Protocol for sprites that are drawable."""

    @abstractmethod
    def draw(self, screen: Surface) -> None:
        """Draws a given sprite to the screen."""
        ...
