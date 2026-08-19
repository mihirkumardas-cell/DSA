n=4
for i in range(2*n-1):
    for j in range(2*n-1):
        top=i
        bottom=2*n-2-i
        left=j
        right=2*n-2-j
        print(n-min(top,bottom,left,right),end=" ")
    print()

