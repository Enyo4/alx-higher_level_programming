#!/usr/bin/python3
def weight_average(my_list=[]):
    """Returns the weighted average of all integers tuple (<score>, <weight>

    Args:
        my_list: List containing tuple (score and weight)

    Returns: 0 if list is empty
    """
    if my_list is None:
        return 0

    total = 0
    div = 0
    for tup in my_list:
        total += tup[0] * tup[1]
        div += tup[1]

    return (total/div)
