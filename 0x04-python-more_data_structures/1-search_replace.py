#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replaces all the occurences of an element by another in a new list.

    Args:
        @mylist: The initial list
        @search: The element to replace in the list
        @replace: The new element

    Returns: The new list
    """
    new_list = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[i])

    return (new_list)
