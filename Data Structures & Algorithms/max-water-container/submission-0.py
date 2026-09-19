class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        area = 0
        while left < right:
            area = max(area,abs(left-right) * min(heights[left], heights[right]))
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return area