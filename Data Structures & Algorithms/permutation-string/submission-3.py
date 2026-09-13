class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        m, n = len(s1), len(s2)
        need, window = [0] * 26, [0] * 26
        base = ord('a')
        
        for i in range(m):
            need[ord(s1[i]) - base] += 1
            window[ord(s2[i]) - base] += 1
    
        if need == window:
            return True
        
        for r in range(m, n):
            window[ord(s2[r - m]) - base] -= 1
            window[ord(s2[r]) - base] += 1

            if need == window:
                return True
        return False