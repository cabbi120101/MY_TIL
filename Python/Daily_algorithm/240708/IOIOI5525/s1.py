N = int(input())
M =  int(input())
S = input().strip()
def count_PN(N, M, S):
    count = 0
    i = 0
    pattern_count = 0  # 'IOI' 패턴의 반복 횟수를 저장하는 변수

    while i < M - 1:
        # 'IOI' 패턴을 찾는다
        if S[i:i+3] == 'IOI':
            pattern_count += 1
            i += 2  # 'OI' 다음 위치로 이동

            # N번의 'OI'가 모이면 PN 패턴이 된다
            if pattern_count == N:
                count += 1
                pattern_count -= 1  # 다음 패턴을 위해 1 감소시킴
        else:
            i += 1
            pattern_count = 0  # 패턴이 깨지면 초기화

    return count

print(count_PN(N, M, S))