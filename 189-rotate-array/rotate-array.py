class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n=len(nums)
        k=k%n
        if n==0 or k==0:
            return nums
        self.reverse(nums,0,n-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,n-1)
    def reverse(self,nums,start,end):
        while start<end:
            nums[start],nums[end]=nums[end],nums[start]
            start+=1
            end-=1
