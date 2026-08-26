class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        l = 0
        r = 1
        n = min(len(word1), len(word2))
        result = ''

        while l < n:
            result = result + word1[l:r] + word2[l:r]
            l,r = l+1, r+1
        if len(word1) > len(word2):
            result = result + word1[l:len(word1)]
        elif len(word1) < len(word2):
            result = result + word2[l:len(word2)]
        return result
        (bad: TC = O(n^2))
        """

        i = 0
        j = 0
        result = []
        m = len(word1)
        n = len(word2)
        while i < m or j < n:
            if i < m:
                result.append(word1[i])
            if j < n:
                result.append(word2[j])
            i = i + 1
            j = j + 1
        return "".join(result)
