#!/usr/bin/python3
def safe_print_integer_err(value):
    """Prints an integer

    Args:
        Value: The input of any type(integer, string, etc.)

    Returns:
        True if value is an integer else,
        False and prints in stderr the error precede by Exception:
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as exc:
        print("Exception: {}".format(exc))
        return False
