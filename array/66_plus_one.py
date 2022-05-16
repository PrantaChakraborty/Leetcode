"""
link: https://leetcode.com/problems/plus-one/
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new_digit = ""
        for item in digits:
            new_digit += str(item)
        new_list = []
        updated_digit = int(new_digit) + 1
        for item in str(updated_digit):
            new_list.append(int(item))
        return new_list


solution = Solution()
digits = [9, 9]
print(solution.plusOne(digits))
