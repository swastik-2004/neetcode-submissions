class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        longest=0
        for n in nums:
            if n-1 not in num_set:
                curr=n
                length=1
                while n+1 in num_set:
                    n+=1
                    length+=1
                longest=max(length,longest)
        return longest
        