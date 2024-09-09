s1 = input()
s2 = input()
s3 = input()

a = len(s1)
b = len(s2)
c = len(s3)
board = [[[0]*(a+1) for _ in range(b+1) ] for _ in range((c+1))]

for i in range(1, c+1):
    for j in range(1, b+1):
        for k in range(1, a+1):
            if s3[i-1] == s2[j-1] == s1[k-1]:
                board[i][j][k] = board[i-1][j-1][k-1] + 1
            else:
                board[i][j][k] = max(board[i-1][j][k],board[i][j-1][k],board[i][j][k-1])          

print(board[c][b][a])
