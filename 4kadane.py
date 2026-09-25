n=int(input())
arr=list(map(int,input().split()))

currsum=arr[0]
maxsum=arr[0]

for i in range(1,n):
    currsum=max(arr[i],currsum+arr[i])
    maxsum=max(maxsum,currsum)

print(maxsum)