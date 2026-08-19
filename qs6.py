n=int(input('enter no of rows:'))
for i in range(n):
    for j in range(n-i):
        print('*',end=' ')
    print()