def print_sorted_dictionary(a_dictionary):
    """ Prints a dictionary by ordered keys.

    Args:
        @a_dictionary: The given dictionary

    Returns: Sorted dictionary
    """
    sub_list = list(a_dictionary.keys())
    sub_list.sort()
    for i in sub_list:
        print("{}: {}".format(i, a_dictionary[i]))
