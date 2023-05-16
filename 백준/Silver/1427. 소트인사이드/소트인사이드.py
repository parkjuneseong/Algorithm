n =int(input())
nn = []
for i in str(n):
    nn.append(int(i))
nn.sort(reverse=1)
for j in nn:
    print(j,end='')