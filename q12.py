n=5
for i in range(n):
    val=1 if i%2==0 else 0
    for j in range(i+1):
        print(val,end=' ')
        val=1-val
    print()