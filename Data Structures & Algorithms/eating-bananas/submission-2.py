class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            m = l + (r - l) // 2
            if self.spendHrs(piles, m) <= h:
                r = m - 1
                res = m
            else:
                l = m + 1
        return res
    
    def spendHrs(self, piles, speed):
        hrs = 0
        for p in piles:
            hrs += math.ceil(float(p) / speed)
        return hrs
