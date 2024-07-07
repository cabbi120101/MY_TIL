N, K = map(int, input().split())
from collections import deque
def bfs(n,k):
    visit = [-1]*100001

    queue = deque([N])
    visit[N] = 0

    while queue:
        temp = queue.popleft()
        if temp == k :
            return visit[temp]

        for next_pos in (temp-1, temp+1, 2*temp):
            if 0<=next_pos<100001 and visit[next_pos]==-1:
                visit[next_pos] = visit[temp]+1
                queue.append(next_pos)

print(bfs(N,K))