n=input('enter a number: ')
count=0
for i in range(len(n)):
    count+=1
print(count)
#another better soln
n=input('enter a number: ')
count=0
for i in(n):
    if i.isdigit():
        count+=1
print(count)
#another brute force soln
n=int(input('enter a number: '))
count=0
while n>0:
    n=n//10
    count+=1
print(count)
#optimal soln with no loops time and space comp=0(1)
import math
n=int(input('enter a number: '))
count=int(math.log10(n))+1
print(count)
