class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        l,h=0,len(arr)
        while l<h:
            m=(l+h)//2
            if arr[m]-(m+1)>=k:
                h=m
            else:
                l=m+1
        return l+k
        