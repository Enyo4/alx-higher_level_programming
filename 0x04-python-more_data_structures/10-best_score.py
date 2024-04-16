#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns a key with the biggest integer value.

    Args:
        a_dictionary: The given dictionary

    Returns:
        The key with the biggest integer value, or None if no score found
    """
    if not a_dictionary:
        return None

    max_score = 0
    max_key = None
    for key, value in a_dictionary.items():
        if a_dictionary[key] > max_score:
            max_score = a_dictionary[key]
            max_key = key

    return max_key
