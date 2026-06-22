class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag=0
        for i in range(len(nums)):
            elem=nums[i]
            for j in range(i+1,len(nums)):
                elem2=nums[j]
                if elem==elem2:
                    flag=flag+1
        if flag>0:
            return True
        else:
            return False