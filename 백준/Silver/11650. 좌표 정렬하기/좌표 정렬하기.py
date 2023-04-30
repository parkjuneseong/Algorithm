n = int(input())
li = []
for i in range(n):
    lis = list(map(int,input().split()))
    li.append([lis[0],lis[1]])
li.sort()
for j in li :
    print(j[0],j[1])