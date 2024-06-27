# Pascal's Triangle Project

This README file provides detailed instructions and guidelines to complete the Pascal's Triangle project, using Python programming.

## Table of Contents

- [Project Overview](#project-overview)
- [Requirements](#requirements)
- [Tasks](#tasks)
  - [0. Pascal's Triangle](#0-pascals-triangle)
- [Resources](#resources)
  - [Primary Resources](#primary-resources)
  - [Additional Resources](#additional-resources)
- [Concepts to Revise](#concepts-to-revise)
- [Repository](#repository)

## Project Overview

This project involves creating a Python function to generate Pascal's Triangle, a classic mathematical structure. Pascal's Triangle has applications in algebra, probability, and number theory. You will apply fundamental Python concepts to develop an efficient algorithm for constructing this triangle.

## Requirements

- Python 3.x
- Basic understanding of lists, loops, functions, and arithmetic operations in Python.

## Tasks

### 0. Pascal's Triangle

**Objective:** Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of `n`.

- The function should return an empty list if `n <= 0`.
- You can assume `n` will always be an integer.

**Example Usage:**

```python
guillaume@ubuntu:~/0x00$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

guillaume@ubuntu:~/0x00$ 
guillaume@ubuntu:~/0x00$ ./0-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
guillaume@ubuntu:~/0x00$ 
```

## Resources

### Primary Resources

- **What is Pascal’s Triangle:** A foundational explanation of Pascal's Triangle and its properties.
- **Pascal’s Triangle - Numberphile:** A video explaining the mathematical concepts behind Pascal's Triangle.

### Additional Resources

- **What are Python Algorithms:** Understanding algorithms in Python and how they can be applied.
- **Mock Technical Interview:** Practice and prepare for technical interviews, focusing on algorithms and problem-solving.

## Concepts to Revise

To successfully complete this project, you should revise the following Python concepts:

- **Lists and List Comprehensions:**
  - Creation, access, modification, and iteration over lists.
  - Utilizing list comprehensions for concise and readable code, especially for generating rows of Pascal’s Triangle.
- **Functions:**
  - Defining and calling functions.
  - Passing parameters and returning values, particularly returning a list of lists representing Pascal’s Triangle.
- **Loops:**
  - Using `for` and `while` loops to iterate through sequences.
  - Nested loops for generating each row and calculating the values of Pascal’s Triangle.
- **Conditional Statements:**
  - Applying `if`, `elif`, and `else` conditions for logic implementation based on the position within Pascal’s Triangle (e.g., edges always being 1).
- **Recursion (Optional):**
  - Understanding recursion as an alternative approach to generating Pascal’s Triangle.
  - Recognizing base cases and recursive cases.
- **Arithmetic Operations:**
  - Performing addition, essential for calculating each element of Pascal’s Triangle as the sum of the two elements directly above it.
- **Indexing and Slicing:**
  - Accessing elements and slices of lists, crucial for identifying and summing correct elements when constructing each row.
- **Memory Management:**
  - Being mindful of how lists are stored and copied, especially when creating new rows based on the values of the previous row.
- **Error and Exception Handling (Optional):**
  - Using `try-except` blocks to handle potential errors, such as invalid input types or values.
- **Efficiency and Optimization:**
  - Considering the time and space complexity of different approaches.
  - Applying optimizations to improve the performance of the solution.

## Repository

- **GitHub Repository:** `alx-interview`
- **Directory:** `0x00-pascal_triangle`
- **File:** `0-pascal_triangle.py`
