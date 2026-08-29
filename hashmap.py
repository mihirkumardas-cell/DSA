from collections import defaultdict
arr=list(map(int,input().split()))
freq_map=defaultdict(int)
for i in arr:
    freq_map[i] += 1
for key,value in freq_map.items():
    print(key,value)