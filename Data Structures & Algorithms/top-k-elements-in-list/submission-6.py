class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1
        
        buckets = [[] for i in range(len(nums) + 1)]
        for key, val in count_dict.items():
            buckets[val].append(key)
        
        result = []
        for bucket in buckets[::-1]:
            for num in bucket:
                result.append(num)
                if len(result) == k:
                    return result