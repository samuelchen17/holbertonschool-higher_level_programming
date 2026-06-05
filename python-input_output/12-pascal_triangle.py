#!/usr/bin/python3


"""pascal triangle"""


def pascal_triangle(n):
    """pascal triangle function"""
    triangle = []

    if n <= 0:
        return triangle

    triangle.append([1])

    if n == 1:
        return triangle

    for row in range(1, n):
        row_arr = []

        for col in range(row + 1):
            if col == 0 or col == row:
                row_arr.append(1)
            else:
                row_arr.append(
                    triangle[row - 1][col - 1] + triangle[row - 1][col]
                )
        triangle.append(row_arr)

    return triangle
