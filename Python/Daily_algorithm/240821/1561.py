N, M = map(int, input().split())
play = list(map(int, input().split()))

# def answer(N,M, play):
#     if N <= M:
#         return N
#     time = 0
#     curr_play = M

#     while curr_play < N:
#         time += 1
#         for i in range(M):
#             if time % play[i] == 0:
#                 curr_play += 1
#                 if curr_play == N:
#                     return i + 1

def answer(N,M,play):
    if N <= M:
        return N
    L, R = 0, max(play)*N
    time = R

    while L <= R:
        mid = (L+R) // 2
        count = M
        for i in play:
            count += mid // i

        if count >= N:
            time = mid
            R = mid - 1
        else:
            L = mid + 1
    count = M
    for i in play:
        count += (time - 1) // i
    
    for i in range(M):
        if time % play[i] == 0:
            count += 1
        if count == N:
            return i + 1
    

print(answer(N,M,play))