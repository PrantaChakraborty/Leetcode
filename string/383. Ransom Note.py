from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransome = Counter(ransomNote)
        maz = Counter(magazine)
        r = ransome - maz
        return not r



ransomNote = "aa"
magazine = "aab"

s = Solution()
print(s.canConstruct(ransomNote, magazine))