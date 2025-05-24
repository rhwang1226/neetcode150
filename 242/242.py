class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len (t):
            return False
        
        lettersS = {}
        lettersT = {}
        for i in range(len(s)):
            lettersS.setdefault(s[i], 0)
            lettersT.setdefault(t[i], 0)
            lettersS[s[i]] += 1
            lettersT[t[i]] += 1
        
        if lettersS == lettersT:
            return True

        else:
            return False