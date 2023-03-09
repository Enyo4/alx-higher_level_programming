#!/usr/bin/python3
def roman_to_int(roman_string):
    rom = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    list = []
    num = 0
    for j in roman_string:
        if j not in rom.keys():
            return None
    for i in range(len(roman_string)):
        a = rom[roman_string[i]]
        if i < len(roman_string)-1 and a < rom[roman_string[i + 1]]:
            num += -(rom[roman_string[i]])
        else:
            num += rom[roman_string[i]]
    return num
