class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        from itertools import permutations
        seen=set()
        for i in permutations(digits,3):
            f,m,l=i
            if f==0:
                continue
            if l%2!=0:
                continue
            nu=f*100+m*10+l
            seen.add(nu)
        return len(seen)
                
            
            
        
        