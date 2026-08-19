n=int(input('enter a number: '))
if n==int(str(n)[::-1]):
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
#another soln
x=int(input('enter a number: '))
text = str(x)
if x < 0:
    print("The number is not a palindrome.")
elif text[:] == text[::-1]:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")