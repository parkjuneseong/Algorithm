n = input()
result = set()
for i in range(len(n)):
    for j in range(i+1,len(n)+1):
        result.add(n[i:j])
print(len(result))