class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        longest=1
        s=set()
        if n==0:
            return 0
        for i in range(n):
            s.add(nums[i])
        for  i  in s:
            if i-1 not in s:
                cnt=1
                x=i
                while x+1 in s:
                    x=x+1
                    cnt+=1
                longest=max(longest,cnt)
        return longest




        
        