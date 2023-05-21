from collections import deque
n,m,v = map(int,input().split())
graph = [[False] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = True
    graph[b][a] = True
visit1 = [False] * (n+1)
visit2 = [False] * (n+1)
def bfs(v):
    q = deque([v])
    visit1[v] = True
    while q :
        v = q.popleft()
        print(v,end=' ')
        for i in range(1,n+1):
            if not visit1[i] and graph[v][i]:
                q.append(i)
                visit1[i] = True


def dfs(v):
    visit2[v] = True
    print(v,end =' ')
    for i in range(1,n+1):
        if not visit2[i] and graph[v][i]:
            dfs(i)
dfs(v)
print()
bfs(v)