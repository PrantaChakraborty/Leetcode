"""
link: https://leetcode.com/problems/single-number/
"""
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_dict = {}
        for item in nums:
            nums_dict[item] = 0
        for item in nums:
            nums_dict[item] += 1
        min_value = min(nums_dict.values())
        for key, value in nums_dict.items():
            if value == min_value:
                return key




#nums = [4, 1, 2, 1, 2, 3, 3]
nums = [4, 3, 3, 3,4, 5]
solution = Solution()
print(solution.singleNumber(nums))
