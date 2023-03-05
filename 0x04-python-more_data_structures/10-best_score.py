#!/usr/bin/python3
def best_score(a_dictionary):
    """ Returns a key with the biggest integer value."""
    if not a_dictionary:
        return None
    else:
        num = []
        for i, j in a_dictionary.items():
            num.append(j)
        max = num[0]
        for x in range(len(num)):
            if num[x] > max:
                max = num[x]        
        return max
