arr=input().split()

group={}

for word in arr:
    key=''.join(sorted(word))

    if key not in group:
        group[key]=[]

    group[key].append(word)

for grou in group.values():
    print(grou)