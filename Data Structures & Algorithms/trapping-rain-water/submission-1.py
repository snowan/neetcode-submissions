class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 2:
            return 0
        
        n = len(height)
        leftMax, rightMax = [0] * n, [0] * n

        leftMax[0] = height[0]
        for curr in range(1, n):
            leftMax[curr] = max(leftMax[curr - 1], height[curr])
        
        rightMax[n - 1] = height[n - 1]
        for curr in range(n - 2, -1, -1):
            rightMax[curr] = max(rightMax[curr + 1], height[curr])
  
        res = 0
        for curr in range(n):  
            res += min(leftMax[curr], rightMax[curr]) - height[curr]


        return res