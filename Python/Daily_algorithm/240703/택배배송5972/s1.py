N, M =  map(int, input().split())

graph = {i: {} for i in range(1, N+1)}
# 그래프 만들때, 최소 가중치로 만들어야 맞음 -> 만들때 계속 갱신해야함
# 두개의 헛간이 하나 이상의 길로 연결됨.
for _ in range(M):
    a, b, c = map(int, input().split())
    if b in graph[a]:
        graph[a][b] = min(graph[a][b], c)
    else:
        graph[a][b] = c

    if a in graph[b]:
        graph[b][a] = min(graph[b][a], c)
    else:
        graph[b][a] = c

import heapq

def dijkstra(graph, start):
    # 시작 노드부터 각 노드까지의 최단 경로를 저장할 딕셔너리, 초기값은 무한대
    ans_path = {node: float('inf') for node in range(1, N+1)}
    ans_path[start] = 0  # 시작 노드의 경로는 0
    stack = []  # 우선순위 큐, (거리, 노드) 형태
    heapq.heappush(stack, (0, start))
    while stack:
        # 현재 노드까지의 최단 거리가 가장 짧은 노드를 꺼냄
        current_dist, current_node = heapq.heappop(stack)

         # 이미 처리된 노드는 무시합니다.
        if current_dist > ans_path[current_node]:
            continue

        # 인접 노드와의 경로를 확인
        for neighbor, weight in graph[current_node].items():
            dist = current_dist + weight  # 인접 노드까지의 새로운 경로 계산
            # 새로운 경로가 기존 경로보다 짧으면 갱신
            if dist < ans_path[neighbor]:
                ans_path[neighbor] = dist
                # 갱신된 경로를 우선순위 큐에 추가
                heapq.heappush(stack, (dist, neighbor))
    
    return ans_path

ans = dijkstra(graph, 1)
print(ans[N])