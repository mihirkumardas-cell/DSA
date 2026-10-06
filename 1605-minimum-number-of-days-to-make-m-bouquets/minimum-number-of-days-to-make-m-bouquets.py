class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        n=len(bloomDay)
        if m*k>n:
            return -1
        def ok(days:int)-> bool:
            nb =adjf=0
            for b in bloomDay:
                adjf=adjf+1 if b<=days else 0
                if adjf==k:
                    nb+=1
                    adjf=0
            return nb>=m
        l,h=min(bloomDay),max(bloomDay)
        while l<h:
            mid=(l+h)//2
            if ok(mid):
                h=mid
            else:
                l=mid+1
        return l
        