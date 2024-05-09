def island_perimeter(grid):
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Check if it's land
                perimeter += 4  # Initialize with 4 sides
                
                # Check adjacent cells
                if i > 0 and grid[i - 1][j] == 1:  # Check up
                    perimeter -= 2  # Subtract if land cell is above
                if j > 0 and grid[i][j - 1] == 1:  # Check left
                    perimeter -= 2  # Subtract if land cell is to the left
    
    return perimeter

# Example usage:
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))  # Output: 12
