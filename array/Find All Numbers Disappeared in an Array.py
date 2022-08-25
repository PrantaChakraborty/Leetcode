from typing import List
import time


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        Let nums = [4, 3, 2, 7, 8, 2, 3, 1]. Now let's iterate through the array nums.

At iter = 0,
current number: |4| (|.| here refers to taking the absolute value)
number at index = 3 (current number - 1): 7
After negation: nums = [4, 3, 2, -7, 8, 2, 3, 1]

At iter = 1
current number: |3|
number at index = 2: 2
After negation: nums = [4, 3, -2, -7, 8, 2, 3, 1]

At iter = 2
current number: |-2|
number at index = 1: 3
After negation: nums = [4, -3, -2, -7, 8, 2, 3, 1]

At iter = 3
current number: |-7|
number at index = 6: 3
After negation: nums = [4, -3, -2, -7, 8, 2, -3, 1]

At iter = 4
current number: |8|
number at index = 7: 1
After negation: nums = [4, -3, -2, -7, 8, 2, -3, -1]

At iter = 5
current number: |2|
number at index = 1: -3
Array stays unchanged: nums = [4, -3, -2, -7, 8, 2, -3, -1]

At iter = 6
current number: |-3|
number at index = 2: -2
Array stays unchanged: nums = [4, -3, -2, -7, 8, 2, -3, -1]

At iter = 7
current number: |-1|
number at index = 0: 4
After negation: nums = [-4, -3, -2, -7, 8, 2, -3, -1]

Now the indices at which there are still positive numbers are the numbers (index+1) that weren't present in the array.


        :param nums:
        :return:
        """
        res = []
        for i in range(len(nums)):
            temp = abs(nums[i]) - 1
            if nums[temp] > 0:
                nums[temp] *= -1
        for i, n in enumerate(nums):
            # here n is the value at index i
            if n > 0:
                res.append(i+1)
        return res


nums = [4,3,2,7,8,2,3,1]
# nums = [1, 1]
# nums = [1, 2, 2, 5, 5, 1]
# nums = []
s = Solution()
print(s.findDisappearedNumbers(nums))