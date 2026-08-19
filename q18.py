N=5
for i in range(N):
    ch=ord('A')
    breakpoint=(2*i+1)//2
    for j in range(N-i-1):
        print(' ',end=' ')
    for j in range(1,2*i+2):
        print(chr(ch),end=' ')
        if j  <=breakpoint:
            ch+=1
        else:
            ch-=1
    print()