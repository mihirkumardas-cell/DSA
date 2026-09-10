class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        res=nums[0]
        maxprod=nums[0]
        minprod=nums[0]
        for i in range(1,n):
            curr=nums[i]
            if curr<0:
                maxprod,minprod=minprod,maxprod
            maxprod=max(curr,maxprod*curr)
            minprod=min(curr,minprod*curr)
            res=max(maxprod,res)
        return res


        