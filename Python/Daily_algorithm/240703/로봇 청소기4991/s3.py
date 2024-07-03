from collections import deque

# a->b까지 최단 거리 구하기
def bfs(board, start):
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dist = [[-1] * w for _ in range(h)]
    stack = deque([start])
    dist[start[0]][start[1]] = 0

    while stack:
        x, y = stack.popleft()
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and board[nx][ny] != 'x' and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                stack.append((nx, ny))
    return dist

from itertools import permutations

# 시작에서 모든 먼지 들를 수 있는 경로 확인
def clean_up(board, pos, target):
    target_list = [pos] + target
    dist = [[0] * len(target_list) for _ in range(len(target_list))]
    
    for i in range(len(target_list)):
        temp_dist = bfs(board, target_list[i])
        for j in range(len(target_list)):
            if i != j:
                dist[i][j] = temp_dist[target_list[j][0]][target_list[j][1]]
                # 만약 하나라도 도달할 수 없으면 -1
                if dist[i][j] == -1:
                    return -1
    
    ans = float('inf')
    for perm in permutations(range(1, len(target_list))):
        current = dist[0][perm[0]]

        for i in range(len(perm) - 1):
            current += dist[perm[i]][perm[i + 1]]

        ans = min(ans, current)

    return ans

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    board = []
    start = None
    target = []
    
    for i in range(h):
        line = list(input().strip())
        board.append(line)
        for j in range(w):
            if line[j] == 'o':
                start = (i, j)
            elif line[j] == '*':
                target.append((i, j))

    ans = clean_up(board, start, target)
    print(ans)
