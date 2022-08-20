from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        length_ = len(arr)
        from_start_to_max_item = False
        from_max_item_to_end = False
        if length_ < 3:
            return False
        max_item = max(arr)
        index_of_max_item = arr.index(max_item)
        for i in range(index_of_max_item):
            if arr[i] >= arr[i + 1]:
                return False
            else:
                from_start_to_max_item = True
        for i in range(index_of_max_item, length_ - 1, 1):
            if arr[i] <= arr[i + 1]:
                return False
            else:
                from_max_item_to_end = True

        if from_start_to_max_item == from_max_item_to_end:
            return True
        else:
            return False


# arr = [2,1]
# arr = [3, 5, 5]
# arr = [0,3,2,1]
arr = [1, 7, 5, 4, 3, 2, 1, 0]
s = Solution()
print(s.validMountainArray(arr))
