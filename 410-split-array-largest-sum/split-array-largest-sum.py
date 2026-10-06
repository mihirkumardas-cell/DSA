class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def ok(lim:int)->bool:
            parts=1
            cur=0
            for x in nums:
                if cur+x > lim:
                    parts+=1
                    cur=0
                cur+=x
            return parts<=k
        l,h=max(nums),sum(nums)
        while l<h:
            m=(l+h)//2
            if ok(m):
                h=m
            else:
                l=m+1
        return l



        