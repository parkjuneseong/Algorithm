import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n,m = map(int,input().split())
graph = [[] for i in range(n+1)]
visit = [0] * (n+1)
def dfs(x): 
    visit[x] = 1
    for nx in graph[x]:
        if not visit[nx]:
            dfs(nx)   
for i in range(m):
    a,b = map(int,input().split())
    graph[a]+=[b]
    graph[b]+=[a]
cnt = 0
for i in range(1,n+1):
    if not visit[i]:
        dfs(i)
        cnt +=1
print(cnt)