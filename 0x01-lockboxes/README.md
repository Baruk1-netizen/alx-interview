# Lockboxes

## Overview
This project involves determining if all boxes can be opened given an initial set of locked boxes, each containing keys to other boxes. This problem can be approached using graph traversal algorithms like Depth-First Search (DFS).

## Prerequisites
- Python 3.4.3 or higher
- Basic understanding of lists and list manipulation in Python
- Basic understanding of graph theory concepts (nodes and edges)
- Knowledge of algorithmic complexity (time and space complexity)
- Understanding of recursion, queues, and stacks in Python

## Concepts
The following concepts are instrumental in solving this problem:
- **Lists and List Manipulation**: Accessing, iterating, and modifying lists.
- **Graph Theory Basics**: Understanding nodes and edges, and traversal algorithms like DFS.
- **Algorithmic Complexity**: Writing efficient algorithms.
- **Recursion**: Some solutions might use a recursive approach.
- **Queue and Stack**: Implementing BFS or DFS.
- **Set Operations**: Keeping track of visited nodes and keys.

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the project is mandatory
- Code should be documented
- Code should use the PEP 8 style (version 1.7.x)
- All files must be executable

## Task

### 0. Lockboxes
- Write a method that determines if all the boxes can be opened.
- Prototype: `def canUnlockAll(boxes)`
- `boxes` is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
- There can be keys that do not have boxes
- The first box `boxes[0]` is unlocked
- Return `True` if all boxes can be opened, else return `False`

### Example Usage
```python
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # False
