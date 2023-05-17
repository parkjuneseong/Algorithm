n = int(input())
li = list(map(int,input().split()))
li.sort()
answer = 0
for i in range(n+1):
    answer += sum(li[0:i])
print(answer)