#!/usr/bin/python3
def roman_to_int(roman_string):
    romVal = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M":1000}
    list = []
    n = 0
    for i in roman_string:
        if i not in romVal.keys():
            return None
        elif len(roman_string) == 1:
           return romVal[i]
        else:
            list.append(i)
            n += int(romVal[i])
            for j in range(len(list)-1):
                if list[j] == "I" and (list[j + 1] == "V" or list[j + 1] == "X"):
                    n -= int(romVal[list[j]] * 2)
    return n
