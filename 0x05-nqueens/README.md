# N Queens Puzzle

**Author**: Baruk1-netizen

## Overview

The N Queens puzzle is a classic problem in computer science and chess. The challenge is to place N non-attacking queens on an N×N chessboard. This means no two queens can be in the same row, column, or diagonal.

This project involves writing a program to solve the N Queens problem for any given value of N, where N must be an integer greater than or equal to 4.

## Usage

To run the program, use the following command:

```
nqueens N
```

- If the user calls the program with the wrong number of arguments, the program will print:

  ```
  Usage: nqueens N
  ```

  Followed by a new line, and exit with the status 1.

- If N is not an integer, the program will print:

  ```
  N must be a number
  ```

  Followed by a new line, and exit with the status 1.

- If N is smaller than 4, the program will print:

  ```
  N must be at least 4
  ```

  Followed by a new line, and exit with the status 1.

## Output

The program prints every possible solution to the N Queens problem, with one solution per line. The solutions are represented as lists of lists, where each inner list contains two integers representing the row and column of a queen on the chessboard.

Example for N=4:

```
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

Example for N=6:

```
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```

The solutions do not need to be printed in any specific order.

## Constraints

- The program is only allowed to import the `sys` module.

## Reference

- [Queen](https://en.wikipedia.org/wiki/Queen_(chess))
- [Backtracking](https://en.wikipedia.org/wiki/Backtracking)

## Repository

- **GitHub repository**: alx-interview
- **Directory**: 0x05-nqueens
- **File**: 0-nqueens.py
