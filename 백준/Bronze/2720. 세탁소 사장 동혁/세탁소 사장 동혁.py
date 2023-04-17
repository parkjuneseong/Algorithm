t = int(input())
change = [25,10,5,1]
for i in range(t):
    c = int(input())
    res = []
    for j in change:
        res.append(c//j)
        c = c%j
    print(*res)