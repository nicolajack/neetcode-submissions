class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hts = {}
        htt = {}
        for i in range(len(s)):
            if hts.get(s[i]):
                hts[s[i]] += 1
            else:
                hts[s[i]] = 1
            if htt.get(t[i]):
                htt[t[i]] += 1
            else:
                htt[t[i]] = 1
        if hts != htt:
            return False
        return True
