class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        maj_num = 0
        for i in nums:
            if count == 0:
                maj_num = i
            if maj_num == i:
                count+=1
            else:
                count-=1
        return maj_num