# UTF-8 Validation

## Overview

This project involves creating a method to determine if a given data set represents a valid UTF-8 encoding. The method will analyze a list of integers, where each integer represents a byte of data, and return a boolean indicating whether the data set conforms to the UTF-8 encoding standard.

## Author

Baruk

## Objective

The goal is to write a method, `validUTF8(data)`, that checks if the input list of integers is a valid UTF-8 encoding.

## Method Signature

```python
def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Parameters:
    data (list): A list of integers, each representing a byte (8 least significant bits).

    Returns:
    bool: True if the data is a valid UTF-8 encoding, else False.
    """
```

## Requirements

- A character in UTF-8 can be 1 to 4 bytes long.
- The data set can contain multiple characters.
- Each integer in the list represents 1 byte of data.
- Only the 8 least significant bits of each integer need to be handled.

## Example

The following is an example of how the `validUTF8` method can be tested:

```python
validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))  # Output: True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # Output: True

data = [229, 65, 127, 256]
print(validUTF8(data))  # Output: False
```

## Repository Structure

- **GitHub Repository**: alx-interview
- **Directory**: 0x04-utf8_validation
- **File**: 0-validate_utf8.py

## Usage

To test the `validUTF8` method, you can run the following:

```bash
carrie@ubuntu:~/0x04-utf8_validation$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))  # Output: True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # Output: True

data = [229, 65, 127, 256]
print(validUTF8(data))  # Output: False

carrie@ubuntu:~/0x04-utf8_validation$
carrie@ubuntu:~/0x04-utf8_validation$ ./0-main.py
True
True
False
carrie@ubuntu:~/0x04-utf8_validation$
```
