class Solution:
    def shadowPairs(self, nums: list[int]) -> int:
        import bisect
        n=len(nums)
        ans=0
        stack=[]
        for x in nums:
            ans+=bisect.bisect_left(stack,x)
            while stack and stack[-1]>x:
                stack.pop()
            stack.append(x)
        return ans

        