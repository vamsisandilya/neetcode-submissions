class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_ele = {}
        result = []
        for i in nums:
            freq_ele[i] = freq_ele.get(i, 0) + 1
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, count in freq_ele.items():
            bucket[count].append(num)
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result