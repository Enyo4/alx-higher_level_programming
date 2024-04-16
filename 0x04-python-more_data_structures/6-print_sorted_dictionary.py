def print_sorted_dictionary(a_dictionary):
    """ Prints a dictionary by ordered keys.

    Args:
        a_dictionary: The given dictionary

    """
    sorted_keys = sorted(a_dictionary.keys())
    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))
