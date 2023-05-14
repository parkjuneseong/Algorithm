n,m = map(int,input().split())
mn = []
cnt = []
for i in range(n):
    mn.append(input())
for a in range(n-7):
    for b in range(m -7):
        w_draw = 0
        b_draw = 0
        for i in range(a,a+8):
            for j in range(b,b+8):
                if(i+j)%2 ==0:
                    if mn[i][j]!='W':
                        w_draw+=1
                    else:
                        b_draw+=1
                else:
                    if mn[i][j]!='W':
                        b_draw+=1
                    else:
                        w_draw+=1
        cnt.append(w_draw)
        cnt.append(b_draw)
print(min(cnt))