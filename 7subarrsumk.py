n=int(input())
arr=list(map(int,input().split()))
k=int(input())

map={0:1}
prefixsum=0
count=0

for i in range(n):
    prefixsum+=arr[i]

    if prefixsum-k in map:
        count+=map[prefixsum-k]

    map[prefixsum]=map.get(prefixsum,0)+1

print(count)