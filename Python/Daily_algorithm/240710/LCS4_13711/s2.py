n = int(input())
s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))

prev = [0] * (n + 1)
curr = [0] * (n + 1)

for i in range(1, n+1):
    for j in range(1, n+1):
            if s2[i-1] == s1[j-1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(prev[j], curr[j - 1])         
    prev, curr = curr, prev
print(prev[n])