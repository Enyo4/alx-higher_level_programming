#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """Replaces or adds keys/value in a dictionary.

    Args:
        a_dictionary: An existing dictionary
        key: A string
        Value: any type of data for the given key
    """
    a_dictionary[key] = value
    return (a_dictionary)
