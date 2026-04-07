"""Tests for the Asteroid class."""

from asteroids.sprites.asteroid import Asteroid
from pytest_mock import MockFixture


def test_Asteroid_split(mocker: MockFixture) -> None:
    """Tests the Asteroid's split method."""
    # Disable file operations
    mocked_open = mocker.patch("builtins.open", mocker.mock_open())  # pyright: ignore[reportUnknownMemberType, reportAny]

    mocked_random = mocker.patch("random.uniform", return_value=40.0)

    asteroid = Asteroid(0, 0, 100)
    asteroid.split()

    mocked_open.assert_called_once()
    mocked_random.assert_called_once_with(20.0, 50.0)
