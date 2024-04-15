def print_sorted_dictionary(a_dictionary):
    """ Prints a dictionary by ordered keys.

    Args:
        @a_dictionary: The given dictionary

    Returns: Sorted dictionary
    """
    for i in sorted(a_dictionary):
        print("{}: {}".format(i, a_dictionary[i]))
