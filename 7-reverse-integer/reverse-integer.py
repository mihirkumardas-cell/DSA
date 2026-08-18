class Solution:
    def reverse(self, x: int) -> int:
        is_neg=x<0
        x=abs(x)
        rev=0
        while x>0:
            rev=rev*10+x%10
            x=x//10
        rev= -rev if is_neg else rev
        if rev<-2**31 or rev>2**31-1:
            return 0
        return rev 

            

        