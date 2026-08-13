class Solution:
    def isValid(self, s: str) -> bool:
        m={")":"(","}":"{","]":"["}
        stack=[]
        for i in s:
            if i not in m:
                stack.append(i)
            else:
                top_ele=stack[-1] if stack else "#"
                if top_ele!=m[i]:
                    return False
                else:
                    stack.pop()
        return False if stack else True
        