#!/usr/bin/python3
for characters in range(97, 123):
    if (chr(characters) == 'q') or (chr(characters) == 'e'):
        continue
    print("{:c}".format(characters), end="")
