# Leetcode 88

"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be
stored inside the array nums1. To accommodate this, nums1 has a length of m + n,
where the first m elements denote the elements that should be merged, and the last
n elements are set to 0 and should be ignored. nums2 has a length of n.

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
"""


def merge(nums1, nums2, m, n):

    x, y = m - 1, n - 1

    for z in range(m + n - 1, -1, -1):
        if x < 0:
            nums1[z] = nums2[y]
            y -= 1
        elif y < 0:
            break
        elif nums1[x] > nums2[y]:
            nums1[z] = nums1[x]
            x -= 1
        else:
            nums1[z] = nums2[y]
            y -= 1
