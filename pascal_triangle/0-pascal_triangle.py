#!/usr/bin/python3


'''
Returns a list of lists representing Pascal’s triangle of n rows.
Returns an empty list if n <= 0.
'''


def pascal_triangle(n):
    '''
    pascal's function that returns a pascal triangle
    '''
    if n <= 0:
        return []

    triangle = [[1]]  # First row is always [1]

    for i in range(1, n):
        row = [1]  # Start each row with 1
        for j in range(1, i):
            # Compute middle values by summing adjacent elements from the
            # previous row
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # End each row with 1
        triangle.append(row)

    return triangle
