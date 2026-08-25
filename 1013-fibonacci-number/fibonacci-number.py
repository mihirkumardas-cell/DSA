class Solution:
    def fib(self, n: int) -> int:
        if n<=0:
            return 0
        else:
            sl=0
            l=1
            for i in range(1,n):
                curr=sl+l
                sl=l
                l=curr
            return l

        