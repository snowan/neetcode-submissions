class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights or len(heights) == 0:
            return 0
        maxArea = 0
        l, r = 0, len(heights) - 1
        while l < r:
            minH = min(heights[l], heights[r])
            maxArea = max(maxArea, minH * (r - l))
            if heights[l] <= heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            


        return maxArea