#!/usr/bin/python3
"""
Function to calculate the perimeter of an island in a grid
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of an island in the given grid.
    
    Args:
        grid (list of list of int): 2D list representing the grid where
                                    0 represents water and 1 represents land.
    
    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check all four directions
                if i == 0 or grid[i-1][j] == 0:  # Check top
                    perimeter += 1
                if i == rows-1 or grid[i+1][j] == 0:  # Check bottom
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:  # Check left
                    perimeter += 1
                if j == cols-1 or grid[i][j+1] == 0:  # Check right
                    perimeter += 1
    
    return perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))  # Output should be 12
