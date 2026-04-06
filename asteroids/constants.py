"""Module containing useful constants."""

import pygame

# Screen resolution
SCREEN_WIDTH: int = 1280
SCREEN_HEIGHT: int = 720

# Player data
PLAYER_RADIUS: float = 20  # Radius of player's ship
LINE_WIDTH: int = 2  # Width of lines that draw the player's ship
TURN_SPEED: float = 300
PLAYER_SPEED: float = 200

# Asteroid data
ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE_SECONDS = 0.8
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

# Keyboard keys
LEFT_KEYS = set([pygame.K_a, pygame.K_LEFT, pygame.K_h])
RIGHT_KEYS = set([pygame.K_d, pygame.K_RIGHT, pygame.K_l])
UP_KEYS = set([pygame.K_w, pygame.K_UP, pygame.K_k])
DOWN_KEYS = set([pygame.K_s, pygame.K_DOWN, pygame.K_j])
