#!/usr/bin/python3
def safe_print_integer(value):
    """Prints an integer with "{:d}".format().

    Args:
        value: Can be of any type

    Returns:
        True if Value has been correctly printed, Otherwise false
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (ValueError, TypeError):
        return (False)
