def binary_search(left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if temp[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

T = int(input())
ans = []

for t in range(1, T + 1):
    N, K = map(int, input().split())
    stock = list(map(int, input().split()))

    temp = [stock[0]]
    for i in range(1, N):
        if stock[i] > temp[-1]:
            temp.append(stock[i])
        else:
            j = binary_search(0, len(temp) - 1, stock[i])
            temp[j] = stock[i]

    if len(temp) >= K:
        ans.append(f"Case #{t}\n1")
    else:
        ans.append(f"Case #{t}\n0")

print("\n".join(ans))