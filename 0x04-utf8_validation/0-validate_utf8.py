#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Validate if the data set represents a valid UTF-8 encoding.
    :param data: List of integers representing the data set
    :return: True if data is a valid UTF-8 encoding, else False
    """
    # Number of bytes in the current UTF-8 character
    number_of_bytes = 0

    # Masks to check the leading bits in a byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    # For each integer in the data list
    for num in data:
        mask = 1 << 7
        if number_of_bytes == 0:
            # Count the number of leading 1's in the first byte
            while mask & num:
                number_of_bytes += 1
                mask = mask >> 1

            # 1 byte character (0xxxxxxx) or continuation byte (10xxxxxx)
            if number_of_bytes == 0:
                continue

            # UTF-8 characters are only between 1 and 4 bytes long
            if number_of_bytes == 1 or number_of_bytes > 4:
                return False
        else:
            # For the next bytes, they must all start with 10xxxxxx
            if not (num & mask1 and not (num & mask2)):
                return False

        # Decrement the number of bytes remaining in the current character
        number_of_bytes -= 1

    # All characters should be completely checked
    return number_of_bytes == 0


# Test cases
if __name__ == "__main__":
    data1 = [65]
    print(validUTF8(data1))  # Expected output: True

    data2 = [80, 121, 116, 104, 111, 110,
             32, 105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data2))  # Expected output: True

    data3 = [229, 65, 127, 256]
    print(validUTF8(data3))  # Expected output: False
