#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element 2 lists.

    Args:
        my_list_1: The first list
        my_list_2: The second list
        list_length: The desited length of the resulting list

    Returns:
        A new list (length = list_length) with all divisions
    """
    result = []
    for i in range(list_length):
        try:
            res = my_list_1[i]/my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        except TypeError:
            print("wrong type")
            res = 0
        finally:
            result.append(res)
    return result
