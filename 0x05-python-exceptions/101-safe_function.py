#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    """Excutes a function safely.

    Args:
        fct: pointer to a function
        args: Arguments to be passed to the function

    Returns:
        The result of the function otherwise None if something happens
    """
    try:
        ret = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    else:
        return ret
