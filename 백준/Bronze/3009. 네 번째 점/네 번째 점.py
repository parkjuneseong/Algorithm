x = []
y = []
for i in range(3):
    xx,yy = map(int,input().split())
    x.append(xx)
    y.append(yy)
for i in range(3):
    if x.count(x[i]) == 1:
        xx = x[i]
    if y.count(y[i]) == 1:
        yy = y[i]
print(xx,yy)