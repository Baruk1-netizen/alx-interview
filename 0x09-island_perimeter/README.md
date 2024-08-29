# Island Perimeter

## Project Overview

The "Island Perimeter" project requires implementing an algorithm to compute the perimeter of an island in a grid. The grid is represented by a 2D array of integers where `1` denotes land and `0` denotes water. The task involves analyzing this grid to determine the perimeter of the island, which is surrounded by water.

## Task Details

**Function Signature:**

```python
def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.
    
    Args:
    grid (List[List[int]]): A 2D list where each cell is either 0 (water) or 1 (land).
    
    Returns:
    int: The perimeter of the island.
    """
```

**Input Constraints:**
- `grid` is a list of lists of integers.
- Each cell in the grid is either `0` (water) or `1` (land).
- Cells are connected horizontally or vertically, but not diagonally.
- The grid is rectangular with its width and height not exceeding 100.
- The grid is completely surrounded by water.
- There is only one island (or none).
- The island does not contain any lakes (water inside that is not connected to the surrounding water).

## Requirements

- **Editors:** Allowed editors are `vi`, `vim`, and `emacs`.
- **Python Version:** The code will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3.
- **File Requirements:**
  - All files should end with a new line.
  - The first line of all files should be `#!/usr/bin/python3`.
  - All files must be executable.
- **Code Style:** Follow PEP 8 style guidelines (version 1.7).
- **Modules:** Do not import any external modules.
- **Documentation:** All functions and modules must be documented.

## Project Files

- **Main Script:** `0-main.py`
  ```python
  #!/usr/bin/python3
  """
  0-main
  """
  island_perimeter = __import__('0-island_perimeter').island_perimeter

  if __name__ == "__main__":
      grid = [
          [0, 0, 0, 0, 0, 0],
          [0, 1, 0, 0, 0, 0],
          [0, 1, 0, 0, 0, 0],
          [0, 1, 1, 1, 0, 0],
          [0, 0, 0, 0, 0, 0]
      ]
      print(island_perimeter(grid))
  ```

- **Implementation File:** `0-island_perimeter.py`
  - This file will contain the implementation of the `island_perimeter` function.

## Resources

- **Python Official Documentation:**
  - [Nested Lists](https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions)
- **GeeksforGeeks Articles:**
  - [Python Multi-dimensional Arrays](https://www.geeksforgeeks.org/multi-dimensional-arrays-python/)
- **TutorialsPoint:**
  - [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm)
- **YouTube Tutorials:**
  - [Python 2D Arrays and Lists](https://www.youtube.com/results?search_query=python+2d+arrays+and+lists)

## Additional Resources

- **Mock Technical Interviews**

## Copyright

© 2024 ALX, All rights reserved.

## Author

- [waltertaya](https://www.github.com/waltertaya)
