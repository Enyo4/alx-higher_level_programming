#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Returns a set of all elements present in only  one set.

    Args:
        set_1: The first set given
        set_2: The second given set

    Returns: A new set of elements in only one set_1 or set_2 but not in both
    """
    return set_1 ^ set_2
