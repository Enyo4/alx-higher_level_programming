#!/usr/bin/python3
def best_score(a_dictionary):
    """ Returns a key with the biggest integer value."""
    if not a_dictionary:
        return None
    else:
        max = 0
        for i, j in a_dictionary.items():
            if a_dictionary[i] > max:
                max = a_dictionary[i]
        for i, j in a_dictionary.items():
            if a_dictionary[i] == max:
                return i
