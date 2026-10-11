class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_set = set(nums)
        return len(count_set) != len(nums)
            

        