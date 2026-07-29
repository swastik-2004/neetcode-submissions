class Solution:

    def encode(self, strs: List[str]) -> str:
        a=""
        for i in strs:
            a+=str(len(i))+":"+i
        return a
    def decode(self, strs: str) -> List[str]:
        ans,i=[],0
        while i<len(strs):
            j=i
            while strs[j]!=":":
                j+=1
            length=int(strs[i:j])
            ans.append(strs[j+1:j+1+length])
            i=j+1+length
        
        return ans
        


