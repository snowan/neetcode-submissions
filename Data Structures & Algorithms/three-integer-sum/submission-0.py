class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            if a > 0: # if first number > 0, cannot get all 3 sum == 0 
                break
            if i > 0 and a == nums[i - 1]: # skip since prev already done the same, no need to duplicate the iterations
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum == 0:
                    res.append([a, nums[l], nums[r]])
                    l, r = l + 1, r - 1
                    # skip duplicates from left 
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1



        return res

    
   