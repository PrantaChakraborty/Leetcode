"""
link: https://leetcode.com/problems/search-insert-position/
"""

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums_len = len(nums)
        for item in range(nums_len):
            if nums[item] == target:
                return item
            else:
                if target > nums[nums_len - 1]:
                    return nums_len  # cause len starts form 1
                elif target > nums[item] and target < nums[item + 1]:
                    return item + 1
                elif target < nums[item]:
                    if item == 0:
                        return 0
                    else:
                        return item - 1
