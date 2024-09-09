from itertools import combinations

n = int(input())
snow = list(map(int, input().split()))

height = []

for i in range(n-1):
    for j in range(i+1, n):
        height.append((snow[i]+snow[j],i,j))

height.sort()

ans = 1e9
for i in range(1,len(height)):
    if height[i][1] != height[i-1][1] and height[i][1] != height[i-1][2] and height[i][2] != height[i-1][1] and height[i][2] != height[i-1][2]:
        ans = min(ans, height[i][0]-height[i-1][0])
print(ans)