from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_list = list()
        for num in nums:
            new_list.append(num**2)
        return sorted(new_list)


# nums = [-4,-1,0,3,10]
nums = [-7,-3,2,3,11]
s = Solution()
print(s.sortedSquares(nums))