class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        cnt1=0
        cnt2=0
        el1=float('-inf')
        el2=float('-inf')
        for i in nums:
            if cnt1==0 and el2!=i:
                cnt1=1
                el1=i
            elif cnt2==0 and el1!=i:
                cnt2=1
                el2=i
            elif i==el1:
                cnt1+=1
            elif i==el2:
                cnt2+=1
            else:
                cnt1-=1
                cnt2-=1
        cnt1,cnt2=0,0
        for i in nums:
            if el1==i:
                cnt1+=1
            if el2==i:
                cnt2+=1
        mini=n//3+1
        res=[]
        if cnt1>=mini:
            res.append(el1)
        if cnt2>=mini and el2!=el1:
            res.append(el2)
        return res
            

