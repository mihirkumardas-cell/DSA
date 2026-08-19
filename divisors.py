n=int(input('enter a number: '))
for i in range(1,n+1):
    if n%i==0:
        print(i)#brute force
#optimal
import math
res=[]
n=int(input('enter a number: '))
for i in range(1,int(math.sqrt(n))+1):
    if n%i==0:
        res.append(i)
        if i!=n//i:#2 factors might be same 6
            res.append(n//i)
            res.sort()
print(res)