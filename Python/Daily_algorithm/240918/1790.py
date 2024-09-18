N, k = map(int, input().split())

def find_kth_digit(N, k):
    length = 0  # 현재 자리수에서의 총 자리수 길이
    digit = 1   # 자리수 (1자리, 2자리, 3자리...)
    start = 1   # 해당 자리수에서의 시작 숫자
    
    # N까지 자리수의 범위를 파악하면서 k번째 자리가 어디에 속하는지 찾는다.
    while k > length + (N - start + 1) * digit:
        count = 9 * start * digit  # 현재 자리수 범위에서 차지하는 자리수 개수
        if k <= length + count:
            break
        length += count
        start *= 10
        digit += 1
    
    # k가 포함된 자리수를 찾은 후 k번째 자리가 해당 자리수의 몇 번째인지 계산
    count = (N - start + 1) * digit
    if k > length + count:
        return -1
    
    # 해당 자리수에서 몇 번째 숫자에 있는지 계산
    num_index = (k - length - 1) // digit
    num = start + num_index
    
    # 그 숫자의 몇 번째 자리인지 계산
    digit_index = (k - length - 1) % digit
    return str(num)[digit_index]

print(find_kth_digit(N, k))


N, k = map(int, input().split())

length = 0  # 현재까지 본 자리수의 총 길이
digit = 1   # 자리수 (1자리, 2자리, 3자리...)
start = 1   # 해당 자리수에서의 시작 숫자

while True:
    # 현재 자리수에서 사용할 수 있는 숫자의 범위는 N과 비교하여 제한해야 함
    end = min(N, start * 10 - 1)  # 해당 자리수에서 끝나는 숫자
    count = (end - start + 1) * digit  # 해당 자리수에서 차지하는 자리수의 길이

    if k <= length + count:  # k번째 자리가 해당 자리수 범위 안에 있는지 확인
        break

    length += count  # 해당 자리수 범위에서 차지하는 자리수 더하기
    start *= 10      # 다음 자리수 범위로 이동 (1 -> 10 -> 100 ...)
    digit += 1       # 자리수 증가

# k번째 자리를 찾기 위한 계산
num_index = (k - length - 1) // digit  # 해당 자리에서 몇 번째 숫자인지
num = start + num_index  # 실제 숫자 계산

if num > N:  # N을 초과하면 숫자가 없으므로 -1
    print(-1)
else:
    # 그 숫자의 몇 번째 자리인지 계산
    digit_index = (k - length - 1) % digit
    print(str(num)[digit_index])  # k번째 자리에 해당하는 숫자 출력



N, k = map(int, input().split())

length = 0  # 현재까지 본 자리수의 총 길이
digit = 1   # 자리수
start = 1   # 해당 자리수에서의 시작 숫자

while True:
    end = min(N, start * 10 - 1) 
    count = (end - start + 1) * digit  

    if k <= length + count:
        break

    length += count 
    start *= 10
    digit += 1 

num_index = (k - length - 1) // digit 
num = start + num_index  

if num > N:
    print(-1)
else:
    digit_index = (k - length - 1) % digit
    print(str(num)[digit_index]) 






N, k = map(int, input().split())

length = 0  # 현재까지 본 자리수의 총 길이
digit = 1   # 자리수
start = 1   # 해당 자리수에서의 시작 숫자

while True:
    end = min(N, start * 10 - 1)  # 해당 자리수의 끝 숫자
    count = (end - start + 1) * digit  # 현재 자리수 범위의 자리수 총합

    if k <= length + count:  # k번째 자리가 이 범위 안에 있는지 확인
        break

    length += count  # 현재 자리수 범위에서 차지하는 자리수 더하기
    start *= 10  # 다음 자리수의 시작 숫자
    digit += 1  # 자리수 증가

# k번째 자리가 포함된 숫자 계산
num_index = (k - length - 1) // digit  # 해당 자리에서 몇 번째 숫자인지
num = start + num_index  # 실제 숫자 계산

# 숫자가 N을 초과할 수 있으므로 확인
if num > N:
    print(-1)
else:
    # 그 숫자의 몇 번째 자리인지 계산
    digit_index = (k - length - 1) % digit
    print(str(num)[digit_index])  # k번째 자리에 해당하는 숫자 출력



N, k = map(int, input().split())

length = 0  # 현재까지 본 자리수의 총 길이
digit = 1   # 자리수
start = 1   # 해당 자리수에서의 시작 숫자

while True:
    # 현재 자리수에서의 숫자의 개수
    num_count = 9 * start
    # 해당 자리수에서 차지하는 자리수의 총합
    count = num_count * digit

    if k <= length + count: 
        break

    length += count 
    start *= 10 
    digit += 1 

# k번째 자리가 포함된 숫자 계산
num_index = (k - length - 1) // digit 
num = start + num_index 

# 숫자가 N을 초과할 수 있으므로 확인
if num > N:
    print(-1)
else:
    digit_index = (k - length - 1) % digit
    print(str(num)[digit_index]) 