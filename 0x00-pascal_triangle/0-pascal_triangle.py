def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.
    
    Args:
        n (int): The number of rows to generate.
        
    Returns:
        list of lists: Pascal's Triangle up to the nth row.
    """
    triangle = []
    
    if n <= 0:
        return triangle
    
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, len(row) - 1):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    
    return triangle

# Test the function
if __name__ == "__main__":
    triangle = pascal_triangle(5)
    for row in triangle:
        print(row)
