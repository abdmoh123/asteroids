"""Tests for the utils module."""

import pygame
from asteroids.utils import Key, KeysList, any_keys_in


def test_any_keys_in_valid() -> None:
    """Tests the any_keys_in function."""
    key_inputs: set[Key] = set( [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s] )

    # Populate a dict of keys with the test inputs
    key_dict: dict[Key, bool] = {}
    for key in key_inputs:
        key_dict[key] = True

    # Convert it to a list of booleans to match ScancodeWrapper
    bool_list: KeysList = [key_dict.get(i, False) for i in range(max(key_inputs) + 1)]

    assert any_keys_in(key_inputs, bool_list)


def test_any_keys_in_invalid() -> None:
    """Tests the any_keys_in function."""
    key_inputs: set[Key] = set([pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s])
    actual_inputs: set[Key] = set([pygame.K_f])

    # Populate a dict of keys with the test inputs
    key_dict: dict[Key, bool] = {}
    for key in actual_inputs:
        key_dict[key] = True

    # Convert it to a list of booleans to match ScancodeWrapper
    bool_list: KeysList = [key_dict.get(i, False) for i in range(max(key_inputs | actual_inputs) + 1)]

    assert not any_keys_in(set(key_inputs), bool_list)


def test_any_keys_in_empty() -> None:
    """Tests the any_keys_in function."""
    key_inputs: set[Key] = set([pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s])
    actual_inputs: set[Key] = set()

    # Populate a dict of keys with the test inputs
    key_dict: dict[Key, bool] = {}
    for key in actual_inputs:
        key_dict[key] = True

    # Convert it to a list of booleans to match ScancodeWrapper
    bool_list: KeysList = [key_dict.get(i, False) for i in range(max(key_inputs) + 1)]

    assert not any_keys_in(key_inputs, bool_list)
