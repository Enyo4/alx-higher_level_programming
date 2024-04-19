#!/usr/bin/python3
def raise_exception_msg(message=""):
    """Raises a name exception with a message

    Args:
        message: The message to print if NameError is raised
    """
    try:
        raise NameError
    except NameError as msg:
        print(message)
