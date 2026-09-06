class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = []
        for word in strs:
            encoded_str.append(str(len(word)))
            encoded_str.append('#')
            encoded_str.append(word)
        return "".join(encoded_str) 

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j = j + 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            decoded_str.append(s[i:j])
            i = j
        return decoded_str

