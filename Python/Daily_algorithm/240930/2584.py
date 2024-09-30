from collections import deque
M, N, K = map(int, input().split())
board = [[0]*N for _ in range(M)]
for _ in range(K):
    a,b,a1,b1 = map(int,input().split())
    for i in range(b, b1):
        for j in range(a,a1):
            board[i][j] = 1

d = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs(x,y):
    stack = deque([(x,y)])
    board[x][y] = 1
    size = 0

    while stack:
        x,y = stack.popleft()
        size += 1
        for dx,dy in d:
            nx,ny = dx+x, dy+y
            if 0<=nx<M and 0<=ny<N and board[nx][ny] == 0:
                board[nx][ny] = 1
                stack.append((nx,ny))
    return size
area = []
for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            area.append(bfs(i,j))
print(len(area))
print(*sorted(area))

