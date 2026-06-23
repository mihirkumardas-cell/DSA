class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxi = l = r = zeros = 0
        n = len(nums)
        while r<n:
            if nums[r]==0:
                zeros+=1
            while zeros>k:
                if nums[l]==0:
                    zeros-=1
                l+=1
            maxi=max(maxi,r-l+1)
            r+=1
        return maxi


        