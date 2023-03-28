T = int(input())
N = int(input())
price = 0
for i in range(1,N+1):
    a,b = map(int,input().split())
    price = price + (a*b)
if price == T:
    print('Yes')
else:print('No')