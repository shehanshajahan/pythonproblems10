n=int(input())
arr=list(map(int,input().split()))

nums=set(arr)
maxlen=0

for num in nums:
    if num-1 not in nums:
        current=num
        length=1

        while current+1 in nums:
            current+=1
            length+=1

        maxlen=max(maxlen,length)
print(maxlen)
