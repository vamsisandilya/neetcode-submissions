class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum1 = 0
        count = {0:1}
        result = 0
        for num in nums:
            sum1 += num
            if sum1 - k in count:
                result += count[sum1-k] 
            count[sum1] = count.get(sum1, 0) + 1
        return result