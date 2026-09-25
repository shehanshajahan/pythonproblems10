n=int(input())
arr=list(map(int,input().split()))

s=set()
left=0
maxlen=0

for right in range(len(arr)):
    while arr[right] in s:
        s.remove(arr[left])
        left+=1

    s.add(arr[right])
    maxlen=max(maxlen,right-left+1)
print(maxlen)
