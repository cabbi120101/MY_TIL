import heapq
import sys
N= int(sys.stdin.readline())
num = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if num:
            print(-heapq.heappop(num))
        else:
            print(0)
    else:
        heapq.heappush(num, -x)