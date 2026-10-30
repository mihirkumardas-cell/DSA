class Solution:
    def findPeakGrid(self, mat: list[list[int]]) -> list[int]:
        r,c=len(mat),len(mat[0])
        l,h=0,r-1
        while l<h:
            mid=(l+h)//2
            b_c=0
            for i in range(1,c):
                if mat[mid][i]>mat[mid][b_c]:
                    b_c=i
            if mat[mid+1][b_c]>mat[mid][b_c]:
                l=mid+1
            else:
                h=mid
        b_c=0
        for i in range(1,c):
            if mat[l][i]>mat[l][b_c]:
                b_c=i
        return [l,b_c]


        