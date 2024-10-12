#!/usr/bin/python3
def pascal_triangle(n):
    '''
    function def pascal_triangle(n):
    that returns a list of lists of integers
    representing the Pascal’s triangle of n
    '''
    if n <= 0:
        return []
    
    triangle = [[1]]  # For the first row of Pascal's triangle is always [1]
    
    for i in range(1, n):
        # Starting each row with a 1
        row = [1]
        # Computing the values inside the row using values from the previous row
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        # End each row with a 1
        row.append(1)
        triangle.append(row)
    
    return triangle
