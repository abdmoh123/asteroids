"""Base sprite wrapper."""

from abc import ABC
from typing import Any

from pygame import Rect, Surface
from pygame.sprite import AbstractGroup, Sprite


class BaseSprite(Sprite, ABC):
    """Base sprite wrapper."""

    image: Surface
    rect: Rect
    containers: tuple[AbstractGroup[Any], ...]  # pyright: ignore[reportExplicitAny]

    def __init__(self, *groups: AbstractGroup[Any]) -> None:  # pyright: ignore[reportExplicitAny]
        """Constructor for BaseSprite, handles groups and relevant type hints."""
        super().__init__(*groups)
