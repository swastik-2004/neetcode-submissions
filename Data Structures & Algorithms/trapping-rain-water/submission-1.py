class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        maxleft,maxright=height[0],height[-1]
        ans=0
        l,r=1,len(height)-2
        while l<=r:
            if maxleft<=maxright:
                x=maxleft-height[l]
                if x<=0:
                    ans+=0
                else:
                    ans+=x
                maxleft=max(maxleft,height[l])
                l+=1
            else:
                x=maxright-height[r]
                if x<=0:
                    ans+=0
                else:
                    ans+=x
                maxright=max(maxright,height[r])
                r-=1
        return ans