class Solution(object):
    def twoSum(self, nums, target):
        
        ans = [[i,j] for i in range(len(nums)) for j in range(i, len(nums)) if nums[i]+nums[j] == target and i != j][0]
        
        return ans
