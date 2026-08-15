n=5
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    for j in range(i,n-1):
            print(' ',end=' ')
    for j in range(n-1-i):
        print(' ',end=' ')
    for k in range (i+1):
        print('*',end=' ')
    print()
for i in range(n-1,-1,-1):
    for j in range(i):
        print('*',end=' ')
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(n-i):
        print(' ',end=' ')
    for j in range(i):
        print('*',end=' ')
    print()