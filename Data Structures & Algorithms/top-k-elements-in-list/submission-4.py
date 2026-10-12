class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1
        
        # sort dict w.r.t. values
        ranked = sorted(count_dict.items(), key=lambda item: item[1], reverse=True)
        return [num for num, count in ranked[:k]]