# 0x08. Making Change

## Project Overview

The "0. Change comes from within" project is designed to solve the classic coin change problem using Python. The goal is to determine the minimum number of coins required to make a given total amount using a list of coin denominations. This project involves applying dynamic programming and greedy algorithms to achieve an efficient and correct solution.

## Project Details

- **Start Date:** July 22, 2024, 6:00 AM
- **End Date:** July 26, 2024, 6:00 AM
- **Checker Release Date:** July 23, 2024, 6:00 AM
- **Auto Review:** At the deadline

## Problem Statement

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

### Function Prototype

```python
def makeChange(coins, total):
```

### Parameters

- **coins:** A list of integers representing the values of the coins in your possession.
- **total:** An integer representing the total amount you want to achieve.

### Returns

- **Integer:** The fewest number of coins needed to meet the total.
  - If the total is 0 or less, return 0.
  - If the total cannot be met by any number of coins you have, return -1.

### Example

```python
print(makeChange([1, 2, 25], 37)) # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453)) # Output: -1
```

## Concepts Needed

- **Greedy Algorithms:** Understanding how they work and their limitations.
- **Dynamic Programming:** Basic principles, including overlapping subproblems and optimal substructure.
- **Algorithmic Complexity:** Analyzing time and space complexity.
- **Problem-Solving Strategies:** Breaking down problems, iterative vs. recursive approaches.
- **Python Programming:** List manipulations, list comprehensions, efficient looping, and conditionals.

## Resources

- **Python Official Documentation:** [Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html)
- **GeeksforGeeks Articles:**
  - [Coin Change | DP-7](https://www.geeksforgeeks.org/coin-change-dp-7/)
  - [Greedy Algorithm to Find Minimum Number of Coins](https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/)
- **YouTube Tutorials:** [Dynamic Programming - Coin Change Problem](https://www.youtube.com/watch?v=U95O6ddTk3I)

## Additional Requirements

- **Allowed Editors:** vi, vim, emacs
- **Interpreter:** Python 3.4.3 (Ubuntu 20.04 LTS)
- **File Requirements:**
  - Files should end with a new line.
  - The first line of all files should be exactly `#!/usr/bin/python3`.
  - Code should adhere to PEP 8 style (version 1.7.x).
  - All files must be executable.

## Tasks

### Task 0: Change comes from within

Implement the function `makeChange(coins, total)` to solve the coin change problem. 

- **Prototype:** `def makeChange(coins, total)`
- **Returns:** Fewest number of coins needed to meet total or -1 if impossible.

## Repo Information

- **GitHub Repository:** [alx-interview](https://github.com/Simplyneliswa/alx-interview)
- **Directory:** `0x08-making_change`
- **File:** `0-making_change.py`

## Author

- [waltertaya](https://www.github.com/waltertaya)
