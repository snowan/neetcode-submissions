class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_prod, suf_prod = [nums[0]], [nums[n - 1]]
        
        for left in range(1,n):
            right = n - 1 - left
            pre_prod.append(pre_prod[left - 1] * nums[left])
            suf_prod.append(suf_prod[left - 1] * nums[right])

        res = [suf_prod[n-2]]
        for left in range(1,n-1):
            res.append(pre_prod[left-1] * suf_prod[n-2-left])
        res.append(pre_prod[n-2])

        return res

    

    """
    [1,2,4,6]
    pre: [1,2,8,48]
    suf: [6,24,48,48]

    [suf[n-1-left]]
    """