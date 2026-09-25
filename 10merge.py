intervals=[]

n=int(input())

for i in range(n):
    start,end=map(int,input().split())
    intervals.append([start,end])

intervals.sort()

merged=[]

for interval in intervals:
    start=interval[0]
    end=interval[1]
    if not merged or start> merged[-1][1]:
        merged.append([start,end])
    else:
        merged[-1][1]=max(merged[-1][1],end)

for interval in merged:
    print(interval[0],interval[1])