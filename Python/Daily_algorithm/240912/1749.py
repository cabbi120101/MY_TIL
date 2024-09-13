from itertools import combinations

L, C = map(int, input().split())
alp = input().split()
alp.sort()
vowels = {'a', 'e', 'i', 'o', 'u'}

for combination in combinations(alp, L):
    vowel_count = sum(1 for char in combination if char in vowels)
    temp_count = L - vowel_count

    if vowel_count >= 1 and temp_count >= 2:
        print(''.join(combination))
