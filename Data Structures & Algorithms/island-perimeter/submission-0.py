class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited=set()
        m,n=len(grid),len(grid[0])
        def dfs(i,j):
            if i<0 or i>=m or j>=n or j<0 or grid[i][j]==0:
                return 1
            if (i,j) in visited:
                return 0
            visited.add((i,j))
            p=dfs(i+1,j)
            p+=dfs(i-1,j)
            p+=dfs(i,j+1)
            p+=dfs(i,j-1)
            return p

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    return dfs(i,j)

        