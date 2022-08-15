"""
link: https://leetcode.com/problems/number-of-arithmetic-triplets/
"""
from typing import List


class Solution:
    # def arithmeticTriplets(self, nums: List[int], diff: int) -> None:
    #     seen = set()
    #     cnt = 0
    #     for num in nums:
    #         new_diff = num - diff
    #         if new_diff in seen and new_diff - diff in seen:
    #             cnt += 1
    #         seen.add(num)
    #     print(seen)
    #     print(cnt)

    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        cnt = 0
        for num in nums:
            if num + diff in nums and num + (2*diff) in nums:
                cnt += 1
        return cnt




s = Solution()

# nums = [0,1,4,6,7,10]
nums = [4,5,6,7,8,9]
diff = 2
print(s.arithmeticTriplets(nums, diff))




