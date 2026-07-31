class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        ans=[]
        while l<r:
            x=numbers[l]+numbers[r]
            if target==x:
                ans.append(l+1)
                ans.append(r+1)
                return ans
            elif x>target:
                r-=1
            else:
                l+=1
        