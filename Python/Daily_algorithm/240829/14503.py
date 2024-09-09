N, M = map(int, input().split())
r,c,d =  map(int, input().split())

room = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

cleaned = set()
cleaned.add((r, c))

count = 1

while True:
    cleanable = False
    for _ in range(4):
        d = (d + 3) % 4  # 회전
        ny, nx = r + dy[d], c + dx[d]

        if (ny, nx) not in cleaned and room[ny][nx] == 0:
            # 전진
            cleaned.add((ny, nx))
            count += 1
            r, c = ny, nx
            cleanable = True
            break

    if not cleanable:
        # 후진
        ny, nx = r - dy[d], c - dx[d]

        if room[ny][nx] == 1:
            break
        else:
            r, c = ny, nx

print(count)