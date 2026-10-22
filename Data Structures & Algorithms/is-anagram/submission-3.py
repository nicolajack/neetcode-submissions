class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ht1 = {}
        ht2 = {}
        for i in range(len(s)):
            if s[i] in ht1:
                ht1[s[i]] += 1
            else:
                ht1[s[i]] = 1
            if t[i] in ht2:
                ht2[t[i]] += 1
            else:
                ht2[t[i]] = 1
        if ht1 != ht2:
            return False
        return True
        
