class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        window = set()
        max_len = 0

        while right < len(s):
            if s[right] not in window:
                window.add(s[right])
                max_len = max(max_len, right - left + 1)
                right += 1
            else:
                window.remove(s[left])
                left += 1

        return max_len