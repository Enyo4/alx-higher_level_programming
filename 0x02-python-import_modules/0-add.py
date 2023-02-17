#!/usr/bin/python3

if __name__ == "__main__":
    """if __name__ == "__main__": allows you to execute code when the file runs as a script but not when imported as a module""" 
    """Print the sum of 1 and 2."""
    from add_0 import add

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
