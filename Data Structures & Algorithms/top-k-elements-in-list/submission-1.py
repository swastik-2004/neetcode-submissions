from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x=Counter(nums)
        ans=[item[0] for item in x.most_common(k)]
        return ans
        
        