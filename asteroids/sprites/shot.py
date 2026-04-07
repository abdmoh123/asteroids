"""Class for shots fired by the player."""

from typing import override

import pygame
from asteroids.constants import LINE_WIDTH, SHOT_RADIUS
from asteroids.sprites.circleshape import CircleShape, ColorValue
from asteroids.sprites.mixins.drawable import Drawable
from asteroids.sprites.mixins.updatable import Updatable
from pygame.surface import Surface


class Shot(CircleShape, Drawable, Updatable):  # pyright: ignore[reportUnsafeMultipleInheritance]
    """Class for shots fired by the player."""

    def __init__(self, x: float, y: float, radius: float = SHOT_RADIUS) -> None:
        """Constructor for the Shot class."""
        super().__init__(x, y, radius)

    @override
    def draw(
        self,
        screen: Surface,
        color: ColorValue = "white",
        width: int = LINE_WIDTH,
    ) -> None:
        """Draws the player's shot to the screen.

        Args:
            screen: The screen to draw to
            color: The color of the asteroid, defaults to "white"
            width: The width of the lines, defaults to LINE_WIDTH from constants.py
        """
        _ = pygame.draw.circle(
            surface=screen,
            color="white",
            center=self.position,
            radius=self.radius,
            width=width,
        )

    @override
    def update(self, dt: float) -> None:
        """Updates the shot's properties.

        Args:
            dt: The time since the last frame
        """
        self.position += self.velocity * dt  # pyright: ignore[reportUnannotatedClassAttribute]
