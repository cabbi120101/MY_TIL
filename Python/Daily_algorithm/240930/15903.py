import heapq
n, m = map(int, input().split())
card = list(map(int, input().split()))

heapq.heapify(card)

# m번 합체 과정
for _ in range(m):
    one = heapq.heappop(card)
    two = heapq.heappop(card)
    new_card = one + two
    
    heapq.heappush(card, new_card)
    heapq.heappush(card, new_card)

print(sum(card))