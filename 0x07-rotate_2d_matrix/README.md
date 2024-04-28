# Rotate 2D Matrix

## Introduction
This project provides a Python function to rotate a given n x n 2D matrix 90 degrees clockwise. The rotation is performed in-place, meaning the original matrix is modified directly.

## Functionality
The `rotate_2d_matrix(matrix)` function takes a 2D matrix `matrix` as input and rotates it 90 degrees clockwise. The function does not return anything, as the rotation is performed in-place.

## Usage
To use the `rotate_2d_matrix` function, import it into your Python script and pass the 2D matrix as an argument. Here's an example:

```python
from rotate_2d_matrix import rotate_2d_matrix

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotate_2d_matrix(matrix)
print(matrix)
