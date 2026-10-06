class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def ok(cap:int)->bool:
            used,load=1,0
            for w in weights:
                if load+w>cap:
                    used+=1
                    load=0
                load+=w
            return used<=days
        l,h=max(weights),sum(weights)
        while l<h:
            m=(l+h)//2
            if ok(m):
                h=m
            else:
                l=m+1
        return l
        