n=int(input('enter a number'))
for i in range(n):
    for j in range(i):
        print(' ',end=' ')
    for j in range(2*(n-i)-1):
        print('*',end=' ')
    for j in range(i):
        print(' ',end=' ')
    print()
#alternate way if u start from 1 u add+1 for *
    #n=int(input('enter a number'))
#for i in range(1,n+1):
   # for j in range(i):
        #print(' ',end=' ')
    #for j in range(2*(n-i)+1):
        #print('*',end=' ')
    #for j in range(i):
       #print(' ',end=' ')
    #print()
    #rev pyramid