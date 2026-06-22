class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset=[]
        for i in range(len(nums)):
         for j in range(i + 1, len(nums)):
            if nums[i]+nums[j]==target:
                hashset.extend([i,j])
        return hashset
