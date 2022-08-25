from typing import List
"""
https://leetcode.com/problems/container-with-most-water/
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        max_val = 0
        while start < end:
            distance = end - start
            if height[start] <= height[end]:
                value = height[start] * distance
                max_val = max(value, max_val)  # store the max value
                start += 1
            else:
                value = height[end] * distance
                max_val = max(value, max_val)
                end -= 1

        return max_val



height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# height = [1, 1]
# height = [1, 2, 5, 9, 8, 7]
s = Solution()
print(s.maxArea(height))
