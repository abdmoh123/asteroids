"""Main entrypoint for asteroids."""

from dataclasses import dataclass

import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
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
    while True:
        log_state()

        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    return
                case _:
                    pass

        _ = config.screen.fill((0, 0, 0))
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
