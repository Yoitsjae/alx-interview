# Island Perimeter

## Description

This project contains a Python function `island_perimeter` that calculates the perimeter of the island described in a given grid.

## Usage

To use the `island_perimeter` function, import it into your Python script and pass the grid as an argument.

```python
from island_perimeter import island_perimeter

grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

perimeter = island_perimeter(grid)
print(perimeter)  # Output: 12
