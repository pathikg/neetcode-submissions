class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s, count_t = {}, {}
        for char_s in s:
            count_s[char_s] = count_s.get(char_s, 1) + 1
        
        for char_t in t:
            count_t[char_t] = count_t.get(char_t, 1) + 1

        return count_s == count_t
        