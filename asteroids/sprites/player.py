"""The player class."""

from typing import override

import pygame
from asteroids.constants import (
    DOWN_KEYS,
    LEFT_KEYS,
    LINE_WIDTH,
    PLAYER_RADIUS,
    PLAYER_SHOOT_COOLDOWN_SECONDS,
    PLAYER_SHOT_SPEED,
    PLAYER_SPEED,
    RIGHT_KEYS,
    SHOOT_KEYS,
    SHOT_RADIUS,
    TURN_SPEED,
    UP_KEYS,
)
from asteroids.sprites.circleshape import CircleShape, ColorValue
from asteroids.sprites.mixins.drawable import Drawable
from asteroids.sprites.mixins.updatable import Updatable
from asteroids.sprites.shot import Shot
from asteroids.utils import any_keys_in
from pygame.math import Vector2
from pygame.surface import Surface

type Triangle = tuple[Vector2, Vector2, Vector2]


class Player(CircleShape, Drawable, Updatable):  # pyright: ignore[reportUnsafeMultipleInheritance]
    """The Player class.

    Attributes:
        rotation: The rotation of the player
        position: The x, y position of the player
        velocity: The speed and direction the player is moving
        radius: The radius/size of the player, defaults to PLAYER_RADIUS from constants.py
    """

    def __init__(
        self, x: float, y: float, radius: float = PLAYER_RADIUS
    ) -> None:
        """Constructor for Player."""
        super().__init__(x=x, y=y, radius=radius)
        self.rotation: float = 0.0
        self.shot_cooldown_timer: float = 0.0

    def triangle(self) -> Triangle:
        """Get the points of the player's triangle ship."""
        forward = Vector2(0, 1).rotate(self.rotation)
        right = Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a: Vector2 = self.position + forward * self.radius
        b: Vector2 = self.position - forward * self.radius - right
        c: Vector2 = self.position - forward * self.radius + right
        return (a, b, c)

    def rotate(self, dt: float, turn_speed: float = TURN_SPEED) -> None:
        """Sets the rotation of the player ship.

        Args:
            dt: The time since the last frame
            turn_speed: The speed of rotation, defaults to TURN_SPEED from constants.py
        """
        self.rotation += turn_speed * dt

    def move(self, dt: float, player_speed: float = PLAYER_SPEED) -> None:
        """Moves the player forward or backward.

        Args:
            dt: The time since the last frame
            player_speed: The speed of movement, defaults to PLAYER_SPEED from constants.py
        """
        direction = Vector2(0, 1).rotate(self.rotation)
        self.velocity = direction * dt * player_speed  # pyright: ignore[reportUnannotatedClassAttribute]
        self.position += self.velocity  # pyright: ignore[reportUnannotatedClassAttribute]

    def shoot(
        self,
        shot_speed: float = PLAYER_SHOT_SPEED,
        shot_radius: float = SHOT_RADIUS,
    ) -> None:
        """Shots the player's shot.

        Args:
            shot_speed: The speed of the shot, defaults to PLAYER_SHOT_SPEED from constants.py
            shot_radius: The radius or size of the shot, defaults to SHOT_RADIUS from constants.py
        """
        if self.shot_cooldown_timer > 0.0:
            return
        # Reset timer
        self.shot_cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS

        shot = Shot(self.position.x, self.position.y, shot_radius)
        shot.velocity = Vector2(0, 1).rotate(self.rotation) * shot_speed

    @override
    def draw(
        self,
        screen: Surface,
        color: ColorValue = "white",
        width: int = LINE_WIDTH,
    ) -> None:
        """Draws the player to the screen.

        Args:
            screen: The screen to draw to
            color: The color of the player, defaults to "white"
            width: The width of the lines, defaults to LINE_WIDTH from constants.py
        """
        _ = pygame.draw.polygon(
            surface=screen,
            color=color,
            points=list(self.triangle()),
            width=width,
        )

    @override
    def update(self, dt: float) -> None:
        """Updates the player's model.

        Args:
            dt: The time since the last frame
        """
        keys = pygame.key.get_pressed()  # A list of true/false values

        if any_keys_in(LEFT_KEYS, keys):  # Anti-clockwise
            self.rotate(-dt)
        if any_keys_in(RIGHT_KEYS, keys):  # Clockwise
            self.rotate(dt)
        if any_keys_in(UP_KEYS, keys):  # Forward
            self.move(dt)
        if any_keys_in(DOWN_KEYS, keys):  # Backward
            self.move(-dt)
        if any_keys_in(SHOOT_KEYS, keys):  # Shoot
            self.shoot()

        # Cooldown timer (timer resets to 0.3 every time you shoot anyway)
        self.shot_cooldown_timer -= dt
