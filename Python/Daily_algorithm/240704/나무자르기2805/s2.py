N, M = map(int, input().split())
trees = list(map(int, input().split()))

def find_wood(tree, target):
    end, start = max(trees), 0
    result = 0

    while start <= end:
        mid = (start+end)//2
        wood_lengh = sum(map(lambda x: x - mid if x - mid > 0 else 0, tree))

        if wood_lengh >= target:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result

print(find_wood(trees, M))