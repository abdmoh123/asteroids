"""Main entrypoint for asteroids."""

import sys
from dataclasses import dataclass
from typing import Any

import pygame
from asteroids.asteroid_field import AsteroidField
from asteroids.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from asteroids.logger import log_event, log_state
from asteroids.sprites.asteroid import Asteroid
from asteroids.sprites.player import Player
from pygame.sprite import Group
from pygame.surface import Surface


@dataclass(frozen=True)
class GameConfig:
    """A set of data passed to the main game loop."""

    screen: Surface
    clock: pygame.time.Clock
    fps: int = 60


def pygame_init() -> GameConfig:
    """Initialises the pygame instance.

    Returns:
        Pygame screen surface
    """
    _ = pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    return GameConfig(screen=screen, clock=clock)


def pygame_loop(config: GameConfig) -> None:
    """Main pygame loop.

    Args:
        config: The game configuration
    """
    # Actual seconds per frame (first value isn't valid though)
    dt: float = 0.0

    updatable: Group[Any] = Group()  # pyright: ignore[reportExplicitAny]
    drawable: Group[Any] = Group()  # pyright: ignore[reportExplicitAny]
    asteroids: Group[Any] = Group()  # pyright: ignore[reportExplicitAny]

    Player.containers = (updatable, drawable)  # pyright: ignore[reportAttributeAccessIssue]
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    player = Player(  # pyright: ignore[reportUnusedVariable]
        x=config.screen.get_width() / 2, y=config.screen.get_height() / 2
    )

    asteroid_field = AsteroidField()  # pyright: ignore[reportUnusedVariable]

    while True:
        log_state()

        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    return
                case _:
                    pass

        _ = config.screen.fill((0, 0, 0))

        for updatable_object in updatable:  # pyright: ignore[reportAny]
            updatable_object.update(dt)  # pyright: ignore[reportAny]

        for asteroid in asteroids:  # pyright: ignore[reportAny]
            if player.collides_with(asteroid):  # pyright: ignore[reportAny]
                log_event("player_hit")
                print("Game over!")
                sys.exit(0)

        for drawable_object in drawable:  # pyright: ignore[reportAny]
            drawable_object.draw(config.screen)  # pyright: ignore[reportAny]

        pygame.display.flip()

        # Get the time since the last frame
        delta_time_ms = config.clock.tick(config.fps)
        dt = float(delta_time_ms) / 1000.0


def main() -> None:
    """Main entrypoint function for asteroids."""
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame_loop(pygame_init())


if __name__ == "__main__":
    main()
