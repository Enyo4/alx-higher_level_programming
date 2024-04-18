#!/usr/bin/python3
def safe_print_division(a, b):
    """Divides 2 integers and prints the result.

    Args:
        a: The first integer
        b: The divisor

    Returns: Value of the division else None.
    """
    try:
        result = a/b
        return result
    except ZeroDivisionError:
        return None
