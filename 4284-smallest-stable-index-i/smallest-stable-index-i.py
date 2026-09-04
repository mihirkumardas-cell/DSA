class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        suffix_min=[0]*n
        suffix_min[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            suffix_min[i]=min(suffix_min[i+1],nums[i])
        r_max=nums[0]
        for i in range(n):
            r_max=max(r_max,nums[i])
            if r_max-suffix_min[i]<=k:
                return i
        return -1


        