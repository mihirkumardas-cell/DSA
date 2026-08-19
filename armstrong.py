n=int(input('enter a number: '))
k=len(str(n))
m=n
sum=0
while m>0:
    r=m%10
    sum+=r**k
    m=m//10
if sum==n:
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")