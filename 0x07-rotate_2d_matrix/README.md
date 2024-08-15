# 0x07. Rotate 2D Matrix

## Description

This project involves implementing an in-place algorithm to rotate an \( n \times n \) 2D matrix by 90 degrees clockwise. The solution requires a good understanding of matrix manipulation and in-place operations in Python.

## Concepts

### Matrix Representation in Python
- 2D matrices are represented using lists of lists in Python.
- Elements in a 2D matrix can be accessed and modified using their row and column indices.

### In-place Operations
- Operations performed on data without creating a copy of the data structure.
- Important for minimizing space complexity.

### Matrix Transposition
- Swapping rows and columns in a matrix.
- An essential step in the rotation process.

### Reversing Rows in a Matrix
- Reversing the order of elements in each row.
- A crucial step to achieve the 90-degree clockwise rotation.

### Nested Loops
- Used to iterate through 2D data structures like matrices.
- Necessary for modifying elements during matrix transposition and row reversal.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.10)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Code should use the `pycodestyle` style (version 2.8.0)
- No imports are allowed
- All modules and functions must be documented
- All files must be executable

## Task

### 0. Rotate 2D Matrix

**Mandatory**

Given an \( n \times n \) 2D matrix, rotate it 90 degrees clockwise.

- Prototype: `def rotate_2d_matrix(matrix):`
- Do not return anything. The matrix must be edited in-place.
- Assume the matrix will have 2 dimensions and will not be empty.

#### Example

```python
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
```

**Expected Output:**
```
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

## Resources

- Python Official Documentation: [Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- GeeksforGeeks Articles:
  - [Inplace rotate square matrix by 90 degrees](https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/)
  - [Transpose a matrix in Single line in Python](https://www.geeksforgeeks.org/transpose-matrix-single-line-python/)
- TutorialsPoint: [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm)


## Author

- [@waltertaya](https://www.github.com/waltertaya)
