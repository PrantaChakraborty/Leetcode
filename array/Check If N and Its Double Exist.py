from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for i in range(len(arr)):
            if 2*arr[i] in seen or arr[i] / 2 in seen:
                return True
            seen.add(arr[i])
        print(seen)
        return False




arr = [7, 1, 14, 11]
# arr = [10, 2, 5, 3]
# arr = [3,1,7,11]
# arr = [-10,12,-20,-8,15]
# arr = [-16,-13,8]
# arr = [-2,0,10,-19,4,6,-8]
# arr  = [0, 0]
s = Solution()
print(s.checkIfExist(arr))
