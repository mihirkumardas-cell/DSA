class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        pos={}
        for i,v in enumerate(nums):
            if v not in pos:
                pos[v]=[]
            pos[v].append(i)
        cnt=0
        for id in pos.values():
            if len(id)<3:
                continue
            gap=[]
            for j in range(len(id)-1):
                gap.append(id[j+1]-id[j])
            if len(set(gap))==1:
                cnt+=1
        return cnt
            
        
        
        