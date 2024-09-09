import sys
sys.setrecursionlimit(100000)
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1]*n for _ in range(n)]
dir = [(1,0),(0,1),(-1,0),(0,-1)]

def dfs(x,y):
    if dp[x][y] != -1:
        return dp[x][y]

    max_temp = 1
    
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > board[x][y]:
            max_temp = max(max_temp, 1 + dfs(nx, ny))
    dp[x][y] = max_temp
    return dp[x][y]

ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i,j))
print(ans)