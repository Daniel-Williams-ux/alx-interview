#!/usr/bin/python3
"""validUTF8 Funnbytesion"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding
    """
    b = 0
    mem1 = 1 << 7
    mem2 = 1 << 6

    for i in data:
        mem = 1 << 7
        if b == 0:
            while mem & i:
                b += 1
                mem = mem >> 1
            if b == 0:
                continue
            if b == 1 or b > 4:
                return False
        else:
            if not (i & mem1 and not (i & mem2)):
                return False
        b -= 1
    return b == 0
