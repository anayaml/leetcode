class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        reach_end = 0
        while i < len(nums) and i <= reach_end:
            reach_end = max(reach_end, i+nums[i])
            i+=1
        return i == len(nums)