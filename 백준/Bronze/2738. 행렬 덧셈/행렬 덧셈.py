a,b = [],[]
n,m = map(int,input().split())
for i in range(n):
    i = list(map(int,input().split()))
    a.append(i)
for j in range(n):
    j = list(map(int,input().split()))
    b.append(j)
for k in range(n):
    for z in range(m):
        print(a[k][z]+b[k][z], end =' ')
    print()