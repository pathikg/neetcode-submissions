class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_dict = {}
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1
            if count_dict[num] > 1:
                return True 
        
        return False

        