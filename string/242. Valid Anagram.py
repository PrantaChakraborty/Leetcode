"""
https://leetcode.com/problems/valid-anagram/
"""
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) == len(t):
        #     res = Counter(s) - Counter(t)
        #     if len(res) == 0:
        #         return True
        #     else:
        #         return False
        # return False
        return Counter(s) == Counter(t)



# sr = "anagram"
# t = "nagaram"
sr = "abul"
t = "bau"

s = Solution()
print(s.isAnagram(sr, t))