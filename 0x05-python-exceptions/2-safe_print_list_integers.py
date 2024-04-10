#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Prints the first elements of a list and only integers.

    Args:
        my_list: List to print from
        x: the number of elements to access in my_list

    Returns:
        The numbers of integers printed
    """
    ret = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
