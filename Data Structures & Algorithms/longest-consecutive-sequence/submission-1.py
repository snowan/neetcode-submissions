class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        
        numSet = set(nums)
        res = 0
        for num in nums:
            if num - 1 in numSet:
                continue
            curr, cnt = num, 1
            while (curr + 1) in numSet:
                cnt += 1
                curr += 1
            res = max(res, cnt)

        return res