from typing import List
"""
in place
"""

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> list[int]:
        j, length_ = 0, len(nums)
        if nums is not None and len(nums) == 1:
            return nums
        for i in range(length_):
            if nums[i] % 2 == 0:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
                j += 1
        return nums



nums = [3,1,2,4]
# nums = [4, 3, 6, 7, 7, 2, 0, 1]
# nums = [0]
s = Solution()
x = s.sortArrayByParity(nums)
print(s.sortArrayByParity(nums))