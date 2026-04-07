"""Asteroid sprite class."""

import random
from typing import override

import pygame
from asteroids.constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from asteroids.logger import log_event
from asteroids.sprites.circleshape import CircleShape, ColorValue
from asteroids.sprites.mixins.drawable import Drawable
from asteroids.sprites.mixins.updatable import Updatable
from pygame.surface import Surface


class Asteroid(CircleShape, Drawable, Updatable):  # pyright: ignore[reportUnsafeMultipleInheritance]
    """The Asteroid sprite class."""

    def __init__(self, x: float, y: float, radius: float) -> None:
        """Constructor for Asteroid."""
        super().__init__(x, y, radius)

    def split(self, min_angle: float = 20, max_angle: float = 50, speed_up: float = 1.2) -> None:
        """Splits the asteroid into smaller asteroids."""
        self.kill()

        if self.radius < ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        angle = random.uniform(min_angle, max_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        first_asteroid.velocity = self.velocity.rotate(angle) * speed_up
        second_asteroid.velocity = self.velocity.rotate(-angle) * speed_up

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
