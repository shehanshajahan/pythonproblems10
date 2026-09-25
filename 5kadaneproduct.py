n=int(input())
arr=list(map(int,input().split()))

currmax=arr[0]
currmin=arr[0]
maxprod=arr[0]

for i in range(1,n):
    if arr[i]<0:
        currmax,currmin=currmin,currmax

    currmax=max(arr[i],currmax*arr[i])
    currmin=min(arr[i],currmin*arr[i])

    maxprod=max(maxprod,currmax)

print(maxprod)

    