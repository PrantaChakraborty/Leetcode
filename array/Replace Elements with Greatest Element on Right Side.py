from typing import List
"""
inplace 
"""


class Solution:
    # def replaceElements(self, arr: List[int]) -> List[int]:
    #     length_ = len(arr) - 1
    #     for i in range(len(arr)):
    #         if i == length_:
    #             arr[i] = -1
    #         else:
    #             if length_ - i == 1:
    #                 arr[i] = arr[length_]
    #             else:
    #                 arr[i] = max(arr[i + 1:len(arr)])
    #
    #     return arr

    def replaceElements(self, arr: List[int]) -> List[int]:
        mx = tmp = -1
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] > mx:
                tmp = arr[i]
                arr[i] = mx
                mx = tmp
            else:
                arr[i] = mx
        return arr


arr = [17, 18, 5, 4, 6, 1]
# arr = [3, 4, 6, 9, 2, 1, 8]
s = Solution()
print(s.replaceElements(arr))
