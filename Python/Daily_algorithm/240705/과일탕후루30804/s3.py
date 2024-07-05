N = int(input())
tang = list(map(int, input().split()))


def two_point(n, fruits):
    left = 0
    fruits_count = {}
    max_len = 0

    for right in range(N):
        if fruits[right] in fruits_count:
            fruits_count[fruits[right]] += 1
        else:
            fruits_count[fruits[right]] = 1
        
        while len(fruits_count) > 2:
            fruits_count[fruits[left]] -= 1
            if fruits_count[fruits[left]] == 0:
                del fruits_count[fruits[left]]
            left += 1
        
        max_len = max(max_len, right-left +1)
    return max_len

print(two_point(N, tang))