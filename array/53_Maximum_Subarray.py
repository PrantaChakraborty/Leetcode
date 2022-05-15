"""
link: https://leetcode.com/problems/maximum-subarray/
"""
from typing import List


# using brute force
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         if len(nums) == 0:
#             return 0
#         max_sum = 0
#         num_len = len(nums)
#         for i in range(num_len):
#             curr_sum = 0
#             for j in range(i, num_len):
#                 curr_sum += nums[j]
#                 max_sum = max(max_sum, curr_sum)
#         return max_sum


#  using kadane's algorithm
"""
https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        max_ending_here = nums[0]
        max_so_far = nums[0]
        for i in range(1, len(nums)):
            max_ending_here = max(max_ending_here + nums[i], nums[i])
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far



nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
solution = Solution()
print(solution.maxSubArray(nums))
