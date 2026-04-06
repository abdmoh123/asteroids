"""Main entrypoint for asteroids."""

import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from pygame.surface import Surface


def pygame_init() -> Surface:
    """Initialises the pygame instance.

    Returns:
        Pygame screen surface
    """
    _ = pygame.init()
    return pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def pygame_loop(screen: Surface) -> None:
    """Main pygame loop.

    Args:
        screen: Pygame screen surface
    """
    while True:
        log_state()

        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    return
                case _:
                    pass

        _ = screen.fill((0, 0, 0))
        pygame.display.flip()


def main() -> None:
    """Main entrypoint function for asteroids."""
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame_loop(pygame_init())


if __name__ == "__main__":
    main()
