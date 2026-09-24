class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        k = len(s1)
        left = 0

        count1 = {}
        count2 = {}

        for i in range(k):
            count1[s1[i]] = count1.get(s1[i], 0) + 1
            count2[s2[i]] = count2.get(s2[i], 0) + 1

        for right in range(k, len(s2)):
            if count1 == count2:
                return True

            left_char = s2[left]
            count2[left_char] -= 1

            if count2[left_char] == 0:
                del count2[left_char]

            count2[s2[right]] = count2.get(s2[right], 0) + 1
            left += 1

        return count1 == count2