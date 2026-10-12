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
            if bucket:
                for num in bucket:
                    k -= 1
                    result.append(num)
                    if k == 0:
                        break
            if k == 0:
                break
        return result

            