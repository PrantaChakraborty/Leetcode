from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        total_even_number = 0
        for num in nums:
            number_len = len(str(num))
            print(number_len)
            if number_len % 2 == 0:
                total_even_number += 1
        return total_even_number


nums = [555, 901, 482, 1771]
s = Solution()
print(s.findNumbers(nums))