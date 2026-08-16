class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n=len(temp)
        res=[0]*n
        stack=[]
        for i in range(n):
            while stack and temp[i]>temp[stack[-1]]:
                prev_day=stack.pop()
                res[prev_day]=i-prev_day
            stack.append(i)
        return res
            
            
        