def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list of lists: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)
        triangle.append(new_row)

    return triangle


def print_triangle(triangle):
    """
    Prints Pascal's triangle.

    Args:
        triangle (list of lists): Pascal's triangle to print.
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
