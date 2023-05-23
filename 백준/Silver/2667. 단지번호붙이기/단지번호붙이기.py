n = int(input())
graph = []
def dfs(x,y): 
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    count = 1
    graph[x][y] = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
            count += dfs(nx,ny)
    return count
for i in range(n):
    apart = list(map(int,input()))
    graph.append(apart)
ans = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 :
            ans.append(dfs(i,j))
ans.sort()
print(len(ans),*ans,sep='\n')