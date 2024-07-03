N, K = map(int, input().split())

# 이진수에서 1의 개수 세기
def chk_bottle(n):
    return bin(n).count('1')

# 최소 추가 물병 개수 찾기
def find_min(n, k):
    if chk_bottle(n) <= k:
        return 0  # 추가 물병이 필요 없는 경우
    
    ans = 0
    while chk_bottle(n) > k:
        n += 1
        ans += 1
    return ans


print(find_min(N,K))