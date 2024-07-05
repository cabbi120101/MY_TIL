N, M =  map(int, input().split())
cam = []
do = None


for i in range(N):
    temp = list(input())
    cam.append(temp)

    for j in range(M):
        if temp[j] == 'I':
            do = (i,j)

from collections import deque
def bfs(cam, start):
    visit = [[False]*M for _ in range(N)]
    queue = deque([start])
    visit[start[0]][start[1]] = True
    res = 0

    direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x,y = queue.popleft()
        for dx, dy in direct:
            nx, ny = x + dx, y+dy

            if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny]:
                if cam[nx][ny] == "X":
                    continue
                if cam[nx][ny] == "P":
                    res += 1

                visit[nx][ny] = True
                queue.append((nx,ny))
    return res

ans = bfs(cam, do)
if ans > 0:
    print(ans)
else:
    print("TT")