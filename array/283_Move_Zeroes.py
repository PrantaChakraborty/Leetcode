"""
link: https://leetcode.com/problems/move-zeroes/
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        left = 0
        right = 1
        for i in range(length):
            if right < length:
                if nums[left] == 0 and nums[right] == 0:
                    right += 1
                elif nums[left] == 0 and nums[right] != 0:
                    nums[left] = nums[left] + nums[right]
                    nums[right] = nums[left] - nums[right]
                    nums[left] = nums[left] - nums[right]
                    left += 1
                    right += 1
                else:
                    left = i
                    right = i + 1
        return None


# nums = [0, 1, 0, 3, 12]
# nums = [1,0,1]
nums = [4,2,4,0,0,3,0,5,1,0]
# nums = [4,2,4,3,0,0,0,5,1,0]
solution = Solution()
solution.moveZeroes(nums)
