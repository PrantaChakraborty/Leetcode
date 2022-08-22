from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        sorted_heights = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                count += 1
        return count


# heights = [1,1,4,2,1,3]
# heights = [5,1,2,3,4]
# heights = [5, 2, 3, 1, 4]
heights = [1, 2, 3, 4, 5]
s = Solution()
print(s.heightChecker(heights))
