"""
https://leetcode.com/problems/merge-sorted-array/

using two pointers
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]

        return nums1



# nums1 = [1,2,3,0,0,0]
nums1 = [0]
m = 0
nums2 = [1]
n = 1

s = Solution()
print(s.merge(nums1, m, nums2, n))

