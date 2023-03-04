#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element by another in a new list."""
    for num in my_list:
        if num == search:
            num = replace
        new_list += num
    return new_list