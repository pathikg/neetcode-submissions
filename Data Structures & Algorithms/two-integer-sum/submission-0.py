# 1 3 2 6 5 3



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dict = {}
        for i, num in enumerate(nums):
            if index_dict.get(target - num, 0):
                return [index_dict[target - num] - 1, i]
            index_dict[num] = i + 1
