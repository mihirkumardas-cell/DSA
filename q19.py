n=5
for i in range(n):
    for ch in range(ord('A')+n-i-1,ord('A')+n):
        print(chr(ch),end=' ')
    print()