n,m = map(int,input().split())
li = list(map(int,input().split()))
re = 0
for i in range(n-2):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if li[i]+li[j]+li[k] > m :
                continue
            else:
                re = max(re,li[i]+li[j]+li[k])
print(re)