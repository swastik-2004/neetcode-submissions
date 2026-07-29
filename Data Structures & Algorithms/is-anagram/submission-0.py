from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        x=Counter(s)
        y=Counter(t)
        if x==y:
            return True
        else:
            return False

        