"""
You are given an integer array height of length n. There are n vertical lines
drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such
that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented
by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section)
the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
"""


def maxArea(height):
    # 1. use two pointers
    # 2. have a variable 'max_area' to keep track of max area
    # so far
    # 3. area = (distance b/n lines) * (min of the two curr lines)
    # 4. distance = abs(index_of_pointer_2 - index_of_pointer_1)
    # 5. return the curr max area after a pass through the array

    l, r = 0, len(height) - 1
    curr_area = 0
    max_area = 0

    while l < r:
        distance = r - l

        curr_area = distance * min(height[l], height[r])

        if height[l] < height[r]:
            l += 1
        elif height[l] > height[r]:
            r -= 1
        else:
            l += 1

        max_area = max(curr_area, max_area)

    return max_area
