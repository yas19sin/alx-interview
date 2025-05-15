#!/usr/bin/python3
"""
UTF-8 Validation module
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding

    Args:
        data: List of integers representing 1 byte of data each

    Returns:
        True if data is a valid UTF-8 encoding, else return False
    """
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # For each integer in the data array
    for num in data:
        # Get the 8 least significant bits of the number
        byte = num & 0xFF

        # If this is the start of a new UTF-8 character
        if n_bytes == 0:
            # Count how many bytes this character is (looking at first bits)
            if (byte >> 7) == 0:  # 0xxxxxxx (1 byte)
                n_bytes = 0
            elif (byte >> 5) == 0b110:  # 110xxxxx (2 bytes)
                n_bytes = 1
            elif (byte >> 4) == 0b1110:  # 1110xxxx (3 bytes)
                n_bytes = 2
            # 11110xxx (4 bytes)
            elif (byte >> 3) == 0b11110:
                n_bytes = 3
            else:  # Invalid starting byte
                return False
        else:
            # If this byte is a continuation of a UTF-8 character,
            # it should start with 10xxxxxx
            if (byte >> 6) != 0b10:
                return False
            # Decrement the number of bytes we need to process
            n_bytes -= 1

    # If we've finished processing all bytes and we still have
    # bytes to process, then it's an incomplete UTF-8 character
    return n_bytes == 0
