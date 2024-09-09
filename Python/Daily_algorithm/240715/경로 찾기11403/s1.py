N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
        for i in range(N):
            for j in range(N):
                if board[i][k] == 1 and board[k][j] == 1:
                    board[i][j] = 1


for row in board:
    print(" ".join(map(str, row)))