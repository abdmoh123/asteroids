"""Asteroid sprite class."""

from typing import override

import pygame
from asteroids.constants import LINE_WIDTH
from asteroids.sprites.circleshape import CircleShape, ColorValue
from pygame.surface import Surface


class Asteroid(CircleShape):
    """The Asteroid sprite class."""

    def __init__(self, x: float, y: float, radius: float) -> None:
        """Constructor for Asteroid."""
        super().__init__(x, y, radius)

    @override
    def draw(
        self,
        screen: Surface,
        color: ColorValue = "white",
        width: int = LINE_WIDTH,
    ) -> None:
        """Draws the asteroid to the screen.

        Args:
            screen: The screen to draw to
            color: The color of the asteroid, defaults to "white"
            width: The width of the lines, defaults to LINE_WIDTH from constants.py
        """
        _ = pygame.draw.circle(
            surface=screen,
            color=color,
            center=self.position,
            radius=self.radius,
            width=width,
        )

    @override
    def update(self, dt: float) -> None:
        """Updates the asteroid's properties.

        Args:
            dt: The time since the last frame
        """
        self.position += self.velocity * dt  # pyright: ignore[reportUnannotatedClassAttribute]
