N,C = map(int, input().split())
x = [int(input()) for i in range(N)]
x.sort()

start = 1
end = x[-1] - x[0]
ans = 0

while start <= end:
    mid = (start+end) // 2
    count = 1
    temp = x[0]

    for i in range(1,N):
        if x[i] >= temp + mid:
            count += 1
            temp = x[i]
    if count >= C:
        ans = mid
        start = mid + 1

    else:
        end = mid - 1

print(ans)