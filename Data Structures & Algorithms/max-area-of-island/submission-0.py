class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        ans=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    stack=[(i,j)]
                    grid[i][j]=0
                    area=0

                    while stack:
                        r,c=stack.pop()
                        area+=1

                        for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                            nr,nc=r+dr,c+dc

                            if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:
                                grid[nr][nc]=0
                                stack.append((nr,nc))
                    ans=max(ans,area)
        return ans