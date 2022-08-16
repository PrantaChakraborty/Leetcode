"""
can not use extra space
final output [1, 0, 0, 2, 3, 0, 0, 4] for input [1,0,2,3,0,4,5,0]
"""
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        possible_duplicates = 0
        arr_len = len(arr) - 1

        for left in range(arr_len + 1):
            if left > arr_len - possible_duplicates:
                break

            if arr[left] == 0:
                if left == arr_len - possible_duplicates:
                    arr[arr_len] = 0
                    arr_len -= 1
                    break
                possible_duplicates += 1

        last = arr_len - possible_duplicates  # 5

        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + possible_duplicates] = 0
                possible_duplicates -= 1
                arr[i + possible_duplicates] = 0
            else:
                arr[i + possible_duplicates] = arr[i]
        return None


arr = [1, 0, 2, 3, 0, 4, 5, 0]  # last 5

# arr = [1,2, 3]
s = Solution()
print(s.duplicateZeros(arr))
