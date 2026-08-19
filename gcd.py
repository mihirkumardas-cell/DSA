a=int(input('enter a number: '))
b=int(input('enter a number: '))
while a>0 and b>0:
    if a>b:
        a=a%b
    else:
        b=b%a
print("GCD is:", a if a>0 else b)