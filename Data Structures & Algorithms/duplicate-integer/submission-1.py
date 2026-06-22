class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashsetDataType = set()
        for n in nums:
            if n in hashsetDataType:
                return True
            hashsetDataType.add(n)
        return False