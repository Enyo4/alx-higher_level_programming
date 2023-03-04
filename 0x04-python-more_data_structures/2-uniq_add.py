#!/usr/bin/python3
def uniq_add(my_list=[]):
    """ Adds all unique integers in a list (only once for each integer)"""
    a = []
    sum = 0
    for i in my_list:
        if i in a:
            continue
        else:
            a.append(i)
    for i in a:
        sum = sum + i
    return sum