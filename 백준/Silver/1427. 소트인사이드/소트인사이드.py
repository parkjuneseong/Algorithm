n = int(input())
li = []
for i in str(n):
    li.append(int(i))
li.sort(reverse=1)
for j in li:
    print(j,end='')