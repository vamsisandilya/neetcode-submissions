class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        look_up = {}
        for i in range(len(nums)):
            diff = target - nums[i] 
            if diff in look_up:
                return [look_up[diff], i]
            else:
                look_up[nums[i]] = i