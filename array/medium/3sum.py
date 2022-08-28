"""
https://leetcode.com/problems/3sum/
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums) -2):

            # to handle duplicate
            if i > 0 and nums[i] == nums[i-1]:
                continue
            start = i+1
            end = len(nums) - 1
            while start < end:
                sums = nums[i] + nums[start] + nums[end]
                if sums < 0:
                    start += 1
                elif sums > 0:
                    end -= 1
                else:
                    res.append([nums[i], nums[start], nums[end]])
                    # to handle duplicate value
                    while start < end and nums[start] == nums[start+1]:
                        start += 1
                    while end < end and nums[end] == nums[end-1]:
                        end -= 1
                    start += 1
                    end -= 1
        return res




nums = [-1, 0, 1, 2, -1, -4]
s = Solution()
print(s.threeSum(nums))
