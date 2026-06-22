class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        wrd1 = "".join(sorted(s))
        wrd2 = "".join(sorted(t))
        if wrd1==wrd2:
            return True
        else:
            return False
        