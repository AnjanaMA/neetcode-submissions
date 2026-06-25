class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        resu={}
        listret=[]
        for num in nums:
            resu[num] = resu.get(num, 0) + 1
        #sorting the dictionary we made that has map of integers as key and their count as values
        listret=[item[0] for item in sorted(resu.items(), key=lambda item: item[1], reverse=True)[:k]]
        return listret