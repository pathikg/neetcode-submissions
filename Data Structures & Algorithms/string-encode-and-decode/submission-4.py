class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            string += f"{len(word):03d}{word}" # since max length 100
        # print(string)
        return string

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = i + 3
            # print(s[i:j])
            length = int(s[i:j])
            start = j
            end = start + length

            strs.append(s[start:end])

            i = end

            
        return strs

