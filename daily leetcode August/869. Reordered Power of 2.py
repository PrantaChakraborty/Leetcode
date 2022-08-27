"""
https://leetcode.com/problems/reordered-power-of-2/
"""
from collections import Counter


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digits = Counter(str(n))
        for i in range(30):
            if digits == Counter(str(1 << i)):
                return True
        return False


n = 64
s = Solution()
print(s.reorderedPowerOf2(n))