class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        check=set()
        count=0
        for r in range(len(s)):
            while s[r] in check:
                check.remove(s[l])
                l += 1
            check.add(s[r])
            count = max(count, r - l + 1)

        return count

        