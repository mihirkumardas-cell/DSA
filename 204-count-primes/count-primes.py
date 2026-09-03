class Solution:
    def countPrimes(self, n: int) -> int:
        if n<3:
            return 0
        is_comp=[False]*n
        for i in range(2,int(n**0.5)+1):
            if not is_comp[i]:
                for j in range(i*i,n,i):
                    is_comp[j]=True
        return is_comp.count(False)-2

        
        