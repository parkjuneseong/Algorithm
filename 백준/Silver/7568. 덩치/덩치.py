n =int(input())
size = []
for _ in range(n):
    x,y = map(int,input().split())
    size.append((x,y))
for i in size:
    score = 1
    for j in size:
        if i[0]<j[0] and i[1]< j[1]:
            score +=1
    print(score,end=' ')