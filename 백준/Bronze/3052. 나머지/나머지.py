n = []
for _ in range(10):
    i = int(input())
    n.append(i%42)
n = set(n)
print(len(n))