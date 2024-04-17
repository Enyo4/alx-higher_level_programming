#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Deletes keys with a specific value in a dictionary.

    Args:
        a_dictionary: The dictionary to modify
        value: The value to search for and delete its corresponding key

    Returns:
        None. Modifies the  inpur dictionary in-place.
    """
    for i in list(a_dictionary.keys()):
        if a_dictionary[i] is value:
            del a_dictionary[i]
    return a_dictionary
