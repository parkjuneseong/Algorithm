t = int(input())
for i in range(t):
    r,s = map(str,input().split())
    r = int(r)
    s = list(s)
    for j in range(len(s)):
        print(s[j]*r,end = '')
    print()