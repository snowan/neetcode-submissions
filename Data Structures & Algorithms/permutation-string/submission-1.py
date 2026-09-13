class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        for i in range(len(s2) - m + 1):
            if self.isPermutation(s1, s2[i:i + m]):
                return True
        return False
    
    def isPermutation(self, s, t):
        return sorted(s) == sorted(t)