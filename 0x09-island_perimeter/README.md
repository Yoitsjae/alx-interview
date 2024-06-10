# Island Perimeter

## Description

This project contains a Python function `island_perimeter` that calculates the perimeter of the island described in a given grid.

## Requirements
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3
- Your code should use the PEP 8 style (version 1.7)
- You are not allowed to import any module
- All modules and functions must be documented
- All your files must be executable

## Installation
Clone the repository and navigate to the project directory:


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
