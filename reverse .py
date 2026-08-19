n=int(input('enter a number: '))
rev=0
while n>0:
    rev=rev*10+n%10
    n=n//10
print(rev)#this code doesnt handles negative no
#this one does
n=int(input('enter a number: '))
is_negative=n<0
n=abs(n)
rev=0
while n>0:
    rev=rev*10+n%10
    n=n//10
if is_negative:
    rev=-rev
print(rev)


