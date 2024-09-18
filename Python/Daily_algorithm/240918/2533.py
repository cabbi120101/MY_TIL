import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.read

# DFS를 통한 DP 테이블 계산
def dfs(node, parent):
    dp[node][0] = 0 
    dp[node][1] = 1  

    for child in tree[node]:
        if child != parent:
            dfs(child, node)
            dp[node][0] += dp[child][1]  
            dp[node][1] += min(dp[child][0], dp[child][1]) 

data = input().splitlines()
N = int(data[0])
tree = [[] for _ in range(N + 1)]
for line in data[1:]:
    u, v = map(int, line.split())
    tree[u].append(v)
    tree[v].append(u)

dp = [[0, 0] for _ in range(N + 1)] 

dfs(1, -1)

print(min(dp[1][0], dp[1][1]))



import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.read

# DFS를 통한 DP 테이블 계산
def dfs(node, parent):
    dp[node][0] = 0  # node가 얼리 아답터가 아닌 경우
    dp[node][1] = 1  # node가 얼리 아답터인 경우 (자기 자신이 포함되므로 1)

    for child in tree[node]:
        if child != parent:  # 부모로 다시 가지 않도록
            dfs(child, node)
            dp[node][0] += dp[child][1]  # 노드가 얼리 아답터가 아닐 때, 자식은 얼리 아답터여야 함
            dp[node][1] += min(dp[child][0], dp[child][1])  # 노드가 얼리 아답터일 때, 자식은 얼리 아답터일 수도, 아닐 수도 있음

# 입력 처리
data = input().splitlines()
N = int(data[0])
tree = [[] for _ in range(N + 1)]
for line in data[1:]:
    u, v = map(int, line.split())
    tree[u].append(v)
    tree[v].append(u)

# DP 테이블 생성
dp = [[0, 0] for _ in range(N + 1)]  # dp[node][0]: node가 얼리 아답터가 아닐 때, dp[node][1]: node가 얼리 아답터일 때

# DFS로 트리를 순회하며 DP 값 채우기
dfs(1, -1)

# 결과 출력 (루트 노드가 얼리 아답터일 때와 아닐 때 중 최소 값)
print(min(dp[1][0], dp[1][1]))
