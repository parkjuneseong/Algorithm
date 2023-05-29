n,k = map(int,input().split())
li = list(map(int,input().split()))
li.sort(reverse= 1)
print(li[k-1])