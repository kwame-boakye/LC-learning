"""
Given an integer array nums and an integer k,
return the k most frequent elements. You may return the answer in any order.
Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

"""

from collections import Counter


def topKFrequent(nums, k):
    count = Counter(nums)
    ans = []

    sorted_arr = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
    for key in sorted_arr.keys():
        if len(ans) != k:
            ans.append(key)

    return ans
