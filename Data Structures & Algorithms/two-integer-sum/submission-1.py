# 1 3 2 6 5 3



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dict = {}
        for i, num in enumerate(nums):
            if target - num in index_dict:
                return [index_dict[target - num], i]
            index_dict[num] = i
