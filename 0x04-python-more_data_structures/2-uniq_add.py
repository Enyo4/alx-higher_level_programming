#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list(only once for each integer).
    Args:
        @my_list: a list of integers

    Returns: the sum
    """
    sum = 0
    new_list = []
    for num in my_list:
        if num not in new_list:
            new_list.append(num)
    for i in new_list:
        sum += i

    return (sum)
