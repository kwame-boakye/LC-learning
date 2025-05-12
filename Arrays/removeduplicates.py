# Leetcode 26
"""
Remove duplicates from a sorted array

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
"""


def removeDuplicates(nums):
    if not nums:
        return 0

    k = 1  # Pointer for the next unique position

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1

    return k
