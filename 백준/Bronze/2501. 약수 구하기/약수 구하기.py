n,k = map(int,input().split())
nlist = []
for i in range(1,n+1):
    if n%i ==0:
        nlist.append(i)
if len(nlist) < k :
    print(0)
else:
    print(nlist[k-1])