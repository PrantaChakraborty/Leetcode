"""
link: https://leetcode.com/problems/remove-element/
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start = 0
        for v in nums:
            if v != val:
                nums[start] = v
                start += 1
        return start
