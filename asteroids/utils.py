"""Miscellaneous utility functions."""

from collections.abc import Sequence

type Key = int
type KeysList = Sequence[bool]


def any_keys_in(selected_keys: set[Key], keys_list: KeysList) -> bool:
    """Checks if any value in a list of selected keys are in the given keys list.

    Args:
        selected_keys: A list of keys to check
        keys_list: A list of keys to check against

    Returns:
        True if any of the keys in `selected_keys` are in `keys_list`
    """
    return bool(list(filter(lambda key: keys_list[key], selected_keys)))
