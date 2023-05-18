t , price = map(int,input().split())
li = []
for i in range(t):
    li.append(int(input()))
cnt = 0
for i in reversed(range(t)):
    cnt = cnt + price//li[i]
    price = price%li[i]
print(cnt)