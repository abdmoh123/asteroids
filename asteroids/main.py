"""Main entrypoint for asteroids."""

import sys
from dataclasses import dataclass

import pygame
from asteroids.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from asteroids.logger import log_event, log_state
from asteroids.sprites.asteroid import Asteroid
from asteroids.sprites.asteroid_field import AsteroidField
from asteroids.sprites.mixins.collidable import Collidable
from asteroids.sprites.mixins.drawable import Drawable
from asteroids.sprites.mixins.updatable import Updatable
from asteroids.sprites.player import Player
from asteroids.sprites.shot import Shot
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

    updatable: Group[Updatable] = Group()
    drawable: Group[Drawable] = Group()
    asteroids: Group[Collidable] = Group()
    shots: Group[Collidable] = Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, drawable, updatable)

    player = Player(
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

        for updatable_object in updatable:
            updatable_object.update(dt)

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit(0)

            for shot in shots:
                if asteroid.collides_with(shot):
                    if not isinstance(asteroid, Asteroid):
                        continue

                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()

        for drawable_object in drawable:
            drawable_object.draw(config.screen)

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
