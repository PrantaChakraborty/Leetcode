"""
link: https://leetcode.com/problems/intersection-of-two-arrays-ii/
"""

from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums1, nums2 = sorted(nums1), sorted(nums2)
        pt1, pt2 = 0, 0
        while True:
            try:
                if nums1[pt1] > nums2[pt2]:
                    pt2 += 1
                elif nums1[pt1] < nums2[pt2]:
                    pt1 += 1
                else:
                    result.append(nums1[pt1])
                    pt1 += 1
                    pt2 += 1
            except IndexError:
                break

        return result

nums2 = [4, 9, 5, 4]
nums1 = [9, 4, 9, 8, 4, 5]
solution = Solution()
print(solution.intersect(nums1, nums2))
