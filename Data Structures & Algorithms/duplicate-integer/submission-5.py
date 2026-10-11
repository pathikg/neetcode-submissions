class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_set = set(nums)
        if len(count_set) != len(nums):
            return True

        return False

        