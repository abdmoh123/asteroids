"""Tests for the Player class."""


from asteroids.sprites.player import Player
from pygame import Vector2


def test_Player_rotate() -> None:
    """Tests the Player's rotate method."""
    examples: list[Player] = [
        Player(0, 0),
        Player(1, 0),
        Player(0, 1),
    ]

    expected_rotations: list[float] = [
        1.0,
        -1.0,
        0.0,
    ]

    fake_dt = 1.0
    for player, rot in zip(examples, expected_rotations):
        turn_speed = rot / fake_dt
        player.rotate(fake_dt, turn_speed)

    assert [player.rotation for player in examples] == expected_rotations


def test_Player_move() -> None:
    """Tests the Player's move method."""
    examples: list[Player] = [
        Player(0, 0),
        Player(1, 0),
        Player(0, 1),
    ]

    expected_positions: list[Vector2] = [
        Vector2(1.0, 0.0),  # right by 1
        Vector2(0.0, -1.0),  # down by 1
        Vector2(0.0, 0.0),  # up by 1
    ]

    fake_dt = 1.0
    for player, pos in zip(examples, expected_positions):
        relative_pos = pos - player.position

        # Set the player rotation
        rotation = -relative_pos.angle_to(Vector2(0, 1))
        # Behaviour of angle_to results in 90 degrees rotation if not for this
        if relative_pos == Vector2(0, 0):
            rotation = 0.0
        player.rotation = rotation

        # Apply the move
        move_speed = relative_pos.magnitude() / fake_dt
        player.move(fake_dt, move_speed)

    assert [player.position for player in examples] == expected_positions


def test_Player_shoot_cooldown_timer() -> None:
    """Tests the Player's shoot method. Only the cooldown timer is tested."""
    player = Player(0, 0)
    player.shoot(shot_cooldown=1.0)

    assert player.shot_cooldown_timer == 1.0
