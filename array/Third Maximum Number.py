from typing import List


class Solution:
    # def thirdMax(self, nums: List[int]) -> int:
    #     max_num = 0
    #     if nums is not None and len(nums) < 3:
    #         return max(nums)
    #     new_nums = list(set(nums))
    #     if len(new_nums) >= 3:
    #         for _ in range(3):
    #             max_num = max(new_nums)
    #             new_nums.remove(max_num)
    #         return max_num
    #     else:
    #         return max(new_nums)

    def thirdMax(self, nums: List[int]) -> int:
        new_nums = list(set(nums)) # remove the duplicate from the array
        new_nums.sort(reverse=True)
        if len(new_nums) < 3:
            return new_nums[0]
        else:
            return new_nums[2]




# nums = [3,2,1]
# nums = [1,2]
nums = [2,2,3,1]
# nums = [1, 2, 3, 2, 2, 2, 4]
# nums = [1, 1, 2]
s = Solution()
print(s.thirdMax(nums))