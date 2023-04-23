n = int(input())
xx = []
yy = []
for i in range(n):
    x,y = map(int,input().split())
    xx.append(x)
    yy.append(y)
print((max(xx)-min(xx))*(max(yy)-min(yy)))