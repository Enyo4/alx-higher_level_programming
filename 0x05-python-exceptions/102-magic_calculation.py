#!/usr/bin/python3
def magic_calculation(a, b):
    for i in range(1, 4):
        try:
            if i > a:
                raise Exception('Too far')
            result += a ** b / i
        except Exception:
            result = b + a
            break

    return result
