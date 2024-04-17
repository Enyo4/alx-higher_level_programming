#!/usr/bin/python3
def weight_average(my_list=[]):
    """Returns the weighted average of all integers tuple (<score>, <weight>

    Args:
        my_list: List containing tuple (score and weight)

    Returns: 0 if list is empty
    """
    if not my_list or my_list is None:
        return 0

    total = 0
    div = 0
    for score, weight in my_list:
        total += score * weight
        div += weight

        if div == 0:
            return 0

    return (total/div)
