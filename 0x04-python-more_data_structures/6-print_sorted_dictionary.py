def print_sorted_dictionary(a_dictionary):
    """ Prints a dictionary by ordered keys.

    Args:
        a_dictionary: The given dictionary

    """
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
