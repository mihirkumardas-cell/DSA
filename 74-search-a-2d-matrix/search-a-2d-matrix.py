class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        col=len(matrix[0])
        low,high=0,len(matrix)*col-1
        while low<=high:
            mid=(low+high)//2
            val=matrix[mid//col][mid%col]
            if val==target:
                return True
            elif val< target:
                low=mid+1
            else:
                high=mid-1
        return False

        