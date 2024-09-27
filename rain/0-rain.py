#!/usr/bin/python3
'''
Calculate the total amount of rainwater retained after it rains.
'''


def rain(walls):
    """
    Given a list of non-negative integers representing the heights of walls,
    this function computes how many square units of water will be retained
    between the walls.

    Parameters:
    walls:list of non-negative integers representing the heights
                         of walls with unit width 1.

    Returns:
    int: The total amount of rainwater retained. If the input list is empty,
         returns 0.

    Assumptions:
    - The ends of the list  are not walls,
      meaning they will not retain water.
    """

    # Check if the input list is empty
    if not walls:
        return 0

    # Initialize two pointers for left and right ends of the list
    left, right = 0, len(walls) - 1

    # Initialize left_max and right_max to track the maximum heights
    left_max, right_max = walls[left], walls[right]

    # Variable to accumulate the total water retained
    water_retained = 0

    # Process the wall heights until the two pointers meet
    while left < right:
        if left_max < right_max:
            # Move the left pointer towards the right
            left += 1

            # Update left_max if the current wall is taller
            left_max = max(left_max, walls[left])

            # Calculate the water retained above the current wall
            water_retained += left_max - walls[left]
        else:
            # Move the right pointer towards the left
            right -= 1

            # Update right_max if the current wall is taller
            right_max = max(right_max, walls[right])

            # Calculate the water retained above the current wall
            water_retained += right_max - walls[right]

    return water_retained
