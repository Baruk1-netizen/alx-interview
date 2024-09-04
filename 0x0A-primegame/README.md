# 0x0A. Prime Game

## Overview

This project is part of the Curriculum Short Specializations, focusing on algorithms and Python programming. It involves solving a competitive game scenario that requires leveraging an understanding of prime numbers, game theory, and algorithm optimization.

## Concepts Needed

### Prime Numbers
- **Definition**: Prime numbers are natural numbers greater than 1 that have no positive divisors other than 1 and themselves.
- **Algorithms**: Efficient methods for identifying prime numbers within a range, such as the Sieve of Eratosthenes.

### Sieve of Eratosthenes
- An efficient algorithm for finding all prime numbers up to a given limit.
- Steps:
  1. Create a boolean array and initialize all entries as true.
  2. Mark the multiples of each prime number starting from 2.

### Game Theory
- **Principles**: Understanding competitive games where players take turns and the concept of optimal play.
- **Win Conditions**: Strategies that determine a win or loss.

### Dynamic Programming/Memoization
- **Definition**: Using previous results to optimize future calculations.
- **Application**: Useful for optimizing the solution for multiple rounds of the game.

### Python Programming
- **Loops and Conditionals**: Implementing game logic and algorithms.
- **Arrays and Lists**: Storing integers and tracking removed numbers.

## Resources

### Prime Numbers and Sieve of Eratosthenes
- [Khan Academy: Prime Numbers](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:understanding-factors/x2f8bb11595b61c86:prime-numbers/v/prime-numbers)
- [Sieve of Eratosthenes in Python](https://www.geeksforgeeks.org/sieve-of-eratosthenes/)

### Game Theory Basics
- [Game Theory Introduction](https://www.investopedia.com/terms/g/gametheory.asp)

### Dynamic Programming
- [Dynamic Programming with Python Examples](https://realpython.com/python-data-structures/)

### Python Official Documentation
- [Python Lists](https://docs.python.org/3/tutorial/datastructures.html)

## Requirements

### General
- Editors: vi, vim, emacs
- Files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- Code should adhere to PEP 8 style (version 1.7.x)
- All files must be executable

### Tasks

#### 0. Prime Game
Maria and Ben are playing a game with the following rules:
1. Given a set of consecutive integers starting from 1 up to and including `n`.
2. They take turns choosing a prime number from the set and removing that number and its multiples from the set.
3. The player that cannot make a move loses the game.
4. They play `x` rounds of the game, where `n` may be different for each round.
5. Maria always goes first and both players play optimally.

##### Prototype
```python
def isWinner(x, nums):
    # Implementation here
```

- `x`: The number of rounds.
- `nums`: An array of integers representing `n` for each round.
- Return: The name of the player that won the most rounds or `None` if the winner cannot be determined.

##### Example
```python
x = 3
nums = [4, 5, 1]

print(isWinner(x, nums))  # Output: "Ben"
```

##### Example Breakdown
1. **First round (n=4)**
    - Maria picks 2, removes 2 and 4 (remaining: 1, 3)
    - Ben picks 3, removes 3 (remaining: 1)
    - Ben wins
2. **Second round (n=5)**
    - Maria picks 2, removes 2 and 4 (remaining: 1, 3, 5)
    - Ben picks 3, removes 3 (remaining: 1, 5)
    - Maria picks 5, removes 5 (remaining: 1)
    - Maria wins
3. **Third round (n=1)**
    - Ben wins (no prime numbers for Maria to choose)

#### Repository
- **GitHub Repository**: `alx-interview`
- **Directory**: `0x0A-primegame`
- **File**: `0-prime_game.py`

## Author

- [waltertaya](https://www.github.com/waltertaya)
