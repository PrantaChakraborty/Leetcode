"""
https://leetcode.com/problems/rotate-image/
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        start = 0
        end = len(matrix) - 1
        while start < end:
            # reverse the matrix
            # [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
            matrix[start], matrix[end] = matrix[end], matrix[start]
            start += 1
            end -= 1

        for i in range(len(matrix)):
            for j in range(i):
                # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # print(matrix)
        return None



matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s = Solution()
s.rotate(matrix)
