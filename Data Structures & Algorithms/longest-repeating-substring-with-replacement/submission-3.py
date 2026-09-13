class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCnt = {}
        l, res, maxFreq = 0, 0, 0
        for r in range(len(s)):
            charCnt[s[r]] = charCnt.get(s[r], 0) + 1
            maxFreq = max(maxFreq, charCnt[s[r]])

            while (r - l + 1) - maxFreq > k:
                charCnt[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res