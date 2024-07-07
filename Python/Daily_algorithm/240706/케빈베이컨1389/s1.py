N, M = map(int, input().split())
graph = [[1e9]*(N+1) for _ in range(N+1)]

# 자기자신
for i in range(1, N+1):
    graph[i][i] = 0

# 친구
for _ in range(M):
    A, B = map(int, input().split())
    graph[A][B] = 1
    graph[B][A] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1,N+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

# 케빈 베이컨 수 계산
min_bacon = 1e9
result = 0

for i in range(1, N + 1):
    bacon_number = sum(graph[i][1:])
    if bacon_number < min_bacon:
        min_bacon = bacon_number
        result = i

print(result)