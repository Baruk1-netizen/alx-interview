# 0x04. UTF-8 Validation

## Project Overview

This project, "UTF-8 Validation," is a part of the ALX curriculum for specialization in algorithms. It involves creating a method to validate UTF-8 encoding in a dataset using Python. You will leverage bitwise operations, understanding of UTF-8 encoding, and list manipulation to achieve this.

## Concepts and Resources

### Bitwise Operations in Python
- **Understanding Bitwise Operations**: You'll need to manipulate bits using operations like AND (`&`), OR (`|`), XOR (`^`), NOT (`~`), and bit shifts (`<<`, `>>`).
  - [Python Bitwise Operators](https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types)

### UTF-8 Encoding Scheme
- **UTF-8 Encoding Rules**: Learn how characters are encoded into one or more bytes and the patterns that define a valid UTF-8 encoded character.
  - [UTF-8 Wikipedia](https://en.wikipedia.org/wiki/UTF-8)
  - [Characters, Symbols, and the Unicode Miracle](https://www.joelonsoftware.com/2003/10/08/)

### Data Representation
- **Byte-level Data Representation**: Work with data at the byte level and handle the least significant bits (LSB) of integers.
  - [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets](https://www.joelonsoftware.com/articles/Unicode.html)

### List Manipulation in Python
- **Iterating Through Lists**: Understand how to iterate, access elements, and use list comprehensions in Python.
  - [Python Lists](https://docs.python.org/3/tutorial/datastructures.html)

### Boolean Logic
- **Applying Logical Operations**: Make decisions within your program using logical operations.

### Additional Resource
- **Mock Technical Interview**: Practice and prepare for technical interviews.

## Requirements

- **Editors**: vi, vim, emacs
- **Environment**: Ubuntu 20.04 LTS, Python 3.4.3
- **File Requirements**:
  - End with a new line
  - First line should be `#!/usr/bin/python3`
  - Follow PEP 8 style (version 1.7.x)
  - Files must be executable
- **README.md**: A mandatory file at the root of the project folder

## Task

### 0. UTF-8 Validation
- **Objective**: Write a method to determine if a given data set represents a valid UTF-8 encoding.
- **Prototype**: `def validUTF8(data):`
- **Return**: `True` if data is valid UTF-8 encoding, `False` otherwise.
- **Details**:
  - A UTF-8 character can be 1 to 4 bytes long.
  - The dataset can contain multiple characters.
  - Data is represented by a list of integers, each integer represents 1 byte.
  - Only handle the 8 least significant bits of each integer.

### Example Usage
```python
#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))  # Expected output: True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # Expected output: True

data = [229, 65, 127, 256]
print(validUTF8(data))  # Expected output: False
```

## Repository Structure

- **GitHub Repository**: alx-interview
- **Directory**: 0x04-utf8_validation
- **File**: 0-validate_utf8.py

## Licensing
This project is licensed under the [ALX](https://www.alxafrica.com/) program.

## Author

- **@waltertaya**
