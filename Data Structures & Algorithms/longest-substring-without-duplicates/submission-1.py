class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s or len(s) < 1:
            return 0
        l, maxSub = 0, 0
        charSet = set()
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            maxSub = max(maxSub, r - l + 1)

        return maxSub

