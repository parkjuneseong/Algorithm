def dfs(x, y):
    # 상하좌우 방향
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    count = 1  # 현재 단지 내의 집 수
    graph[x][y] = 0  # 현재 위치 방문 처리

    # 상하좌우 인접한 집들을 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 지도 범위를 벗어나지 않고 방문하지 않은 집인 경우
        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
            count += dfs(nx, ny)  # 인접한 집으로 dfs 탐색

    return count


N = int(input())  # 지도의 크기
graph = []  # 지도 정보

# 지도 정보 입력
for _ in range(N):
    row = list(map(int, input()))
    graph.append(row)

result = []  # 각 단지 내의 집 수를 저장할 리스트

# 모든 위치에 대해 탐색
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:  # 집이 있는 경우에만 탐색
            result.append(dfs(i, j))  # 단지 내의 집 수를 구해 결과에 추가

result.sort()  # 단지 내의 집 수를 오름차순으로 정렬

print(len(result))  # 총 단지 수 출력
for count in result:
    print(count)  # 각 단지 내의 집 수 출력