class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target = None
        count = 0
        for i in nums:
            if count == 0:
                target = i
            if i == target:
                count = count + 1
            elif i != target:
                count -= 1
        return target
        