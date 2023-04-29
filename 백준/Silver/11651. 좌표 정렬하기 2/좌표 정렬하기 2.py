n = int(input())
li = []
for i in range(n):
    lis = list(map(int,input().split()))
    li.append([lis[1],lis[0]])
li.sort()
for j in li :
    print(j[1],j[0])