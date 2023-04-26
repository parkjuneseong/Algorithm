n = int(input())
re = 0
for i in range(1,n+1):
    li = list(map(int,str(i)))
    re = i + sum(li)
    if re == n :
        print(i)
        break
    if i == n :
        print(0)