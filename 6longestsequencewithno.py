n=int(input())
arr=list(map(int,input().split()))

seen=set()
left=0
maxlen=0

for right in range(len(arr)):

    while arr[right] in seen:
        seen.remove(arr[left])
        left+=1

    seen.add(arr[right])

    maxlen=max(maxlen,right-left+1)
print(maxlen)
