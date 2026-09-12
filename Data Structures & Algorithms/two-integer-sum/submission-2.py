class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_pos = {}
        for i in range(len(nums)):
            num_pos[nums[i]] = i
        
        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in num_pos and i != num_pos[pair]:
                return [i, num_pos[pair]]
        return []
