#!/usr/bin/python3
def roman_to_int(roman_string):
    """Converts a Roman numeral to an integer

    Args:
        roman_string: The roman string to be converted

    Returns: The value in decimal; 0 if roman_string not a string or None
    """
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0

    if roman_string is None:
        return None

    for i in range(len(roman_string)):
        index = rom_val[roman_string[i]]
        if i < len(roman_string)-1 and index < rom_val[roman_string[i+1]]:
            num -= index
        else:
            num += index

    return num
