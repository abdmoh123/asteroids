"""The player class."""

from typing import override

import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, PLAYER_RADIUS
from pygame.math import Vector2
from pygame.surface import Surface

type Triangle = tuple[Vector2, Vector2, Vector2]
type ColorValue = str | tuple[int, int, int]


class Player(CircleShape):
    """The Player class."""

    def __init__(
        self, x: float, y: float, radius: float = PLAYER_RADIUS
    ) -> None:
        """Constructor for Player."""
        super().__init__(x=x, y=y, radius=radius)
        self.rotation: float = 0.0

    def triangle(self) -> Triangle:
        """Get the points of the player's triangle ship."""
        forward = Vector2(0, 1).rotate(self.rotation)
        right = Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a: Vector2 = self.position + forward * self.radius
        b: Vector2 = self.position - forward * self.radius - right
        c: Vector2 = self.position - forward * self.radius + right
        return (a, b, c)

    @override
    def draw(
        self,
        screen: Surface,
        color: ColorValue = "white",
        width: int = LINE_WIDTH,
    ) -> None:
        _ = pygame.draw.polygon(
            surface=screen,
            color=color,
            points=list(self.triangle()),
            width=width,
        )

    @override
    def update(self, dt: float) -> None:
        raise NotImplementedError()
