#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Deletes a key in a dictionary

    Args:
        a_dictionary: Given dictioinary
        key: The dictionary key to delete

    Returns: The updated dictionary
    """
    if key is not None and key in a_dictionary:
        del a_dictionary[key]

    return (a_dictionary)
