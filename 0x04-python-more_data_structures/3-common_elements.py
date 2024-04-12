#!/usr/bin/python3
def common_elements(set_1, set_2):
    """Returns a set of common elements in two sets

    Arg:
        @set_1: The first set
        @set_2: The second set

    Returns: The common element
    """
    for i in set_1:
        if i in set_2:
            return (i)
