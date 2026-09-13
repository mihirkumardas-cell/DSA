class Solution:
    def cyclicShift(self, n: int, grid: list[list[int]], rowShift: list[int], colShift: list[int]) -> list[list[int]]:
        res=[[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                j1=(j-rowShift[i]+n)%n
                i1=(i-colShift[j1]+n)%n
                res[i1][j1]=grid[i][j]
        return res
        