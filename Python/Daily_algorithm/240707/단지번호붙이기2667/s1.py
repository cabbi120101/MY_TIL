n = int(input())
grid = [list(map(int, input())) for _ in range(n)]

def dfs(x, y, n, grid, visited):
    stack = [(x, y)]
    count = 0

    while stack:
        cx, cy = stack.pop()
        if visited[cx][cy]:
            continue
        visited[cx][cy] = True
        count += 1

        # 상하좌우 이동을 위한 방향 벡터
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 1:
                stack.append((nx, ny))

    return count

def find_complexes(n, grid):
    visited = [[False] * n for _ in range(n)]
    complexes = []

    for i in range(n):
        for j in range(n):
            # 집이 있는 곳이고 방문하지 않은 곳이면 DFS 시작
            if grid[i][j] == 1 and not visited[i][j]:
                size = dfs(i, j, n, grid, visited)
                complexes.append(size)

    return complexes

complexes = find_complexes(n, grid)
complexes.sort()

print(len(complexes))  # 총 단지 수 출력
for size in complexes:
    print(size)  # 각 단지 내 집의 수 출력