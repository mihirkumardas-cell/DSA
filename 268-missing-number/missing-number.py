class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        total_s=0
        actual_s=0
        total_s=n*(n+1)//2
        actual_s=sum(nums)
        return total_s-actual_s
        