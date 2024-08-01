# 0x05. N Queens

## Overview

The **0x05. N Queens** project is a classic algorithmic problem in computer science and mathematics. It involves placing N non-attacking queens on an N×N chessboard. This project will help you understand and implement the backtracking algorithm, a key technique in solving combinatorial problems. 


### Backtracking Algorithms
- **Backtracking** is a general algorithm for finding all (or some) solutions to computational problems by incrementally building candidates to the solutions and abandoning a candidate ("backtracking") as soon as it determines that the candidate cannot possibly be completed to a valid solution.
- [Backtracking Introduction](https://en.wikipedia.org/wiki/Backtracking)

### Recursion
- **Recursion** involves functions calling themselves to solve smaller instances of the same problem.
- [Recursion in Python](https://realpython.com/python-thinking-recursively/)

### List Manipulations in Python
- Handling and manipulating lists to store the positions of queens on the board.
- [Python Lists](https://docs.python.org/3/tutorial/datastructures.html)

### Python Command Line Arguments
- Handling command-line arguments using the `sys` module.
- [Command Line Arguments in Python](https://www.pythonforbeginners.com/system/python-sys-argv)

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
- All files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the folder of the project is mandatorydd
- Your code should use the `PEP 8` style (version 1.7.*)
- All your files must be executable

## Task

### 0. N Queens

#### Description
The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.

#### Usage
```
nqueens N
```
- If the user calls the program with the wrong number of arguments, print `Usage: nqueens N`, followed by a new line, and exit with the status `1`.
- `N` must be an integer greater than or equal to `4`.
  - If `N` is not an integer, print `N must be a number`, followed by a new line, and exit with the status `1`.
  - If `N` is smaller than `4`, print `N must be at least 4`, followed by a new line, and exit with the status `1`.
- The program should print every possible solution to the problem, one solution per line.
- Format: see example below.
- You are only allowed to import the `sys` module.

#### Example
```sh
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]

$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```

## Repository

- **GitHub repository:** `alx-interview`
- **Directory:** `0x05-nqueens`
- **File:** `0-nqueens.py`

## Additional Resources

- **Mock Interview:** [Link to Mock Interview](#)
