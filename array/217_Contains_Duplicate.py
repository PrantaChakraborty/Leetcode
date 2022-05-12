"""
link: https://leetcode.com/problems/contains-duplicate/
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        convert_to_set = set(nums)
        if len(nums) != len(list(convert_to_set)):
            return True
        else:
            return False


