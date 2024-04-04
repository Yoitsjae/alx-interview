#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing bytes of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    if not data:
        return False

    def check_bytes(start, length):
        for i in range(start + 1, start + length):
            if i >= len(data) or (data[i] >> 6) != 0b10:
                return False
        return True

    i = 0
    while i < len(data):
        if (data[i] & 0b10000000) == 0:
            i += 1
        elif (data[i] & 0b11100000) == 0b11000000:
            if not check_bytes(i, 2):
                return False
            i += 2
        elif (data[i] & 0b11110000) == 0b11100000:
            if not check_bytes(i, 3):
                return False
            i += 3
        elif (data[i] & 0b11111000) == 0b11110000:
            if not check_bytes(i, 4):
                return False
            i += 4
        else:
            return False
    return True


if __name__ == "__main__":
    data1 = [65]
    print(validUTF8(data1))  # True

    data2 = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data2))  # True

    data3 = [229, 65, 127, 256]
    print(validUTF8(data3))  # False
