class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        j=0
        r=0
        l=0
        while r<n-1:
            far=0
            for i in range(l,r+1):
                far=max(far,i+nums[i])
            l=r+1
            r=far
            j+=1
        return j
        
        