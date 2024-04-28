def rotate_2d_matrix(matrix):
    """
    Rotate a given 2D matrix 90 degrees clockwise in place.
    
    Args:
    - matrix (list of lists): The 2D matrix to rotate
    
    Raises:
    - ValueError: If the matrix is empty or not square
    """
    if not matrix:
        raise ValueError("Matrix is empty")
    
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("Matrix is not square")
    
    # Perform the transpose of the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row to get the final rotated matrix
    for row in matrix:
        row.reverse()
