"""
https://leetcode.com/problems/valid-anagram/
"""
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            res = Counter(s) - Counter(t)
            if len(res) == 0:
                return True
            else:
                return False
        return False



# sr = "anagram"
# t = "nagaram"
sr = "abul"
t = "balu"

s = Solution()
print(s.isAnagram(sr, t))