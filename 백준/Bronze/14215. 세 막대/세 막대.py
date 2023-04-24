li = sorted(list(map(int,input().split())))
if li[2]<li[0]+li[1]:
    print(sum(li))
else:
    print((li[0]+li[1])*2 -1)