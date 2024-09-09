Z = int(input())

for _ in range(Z):
    n,m = map(int, input().split())
    t = list(map(int, input().split())) 

    lake = [0]+[1]*(n)
    gd = 0
    ans = []
    for i in t:
        if t == 0:
            gd += 1
        else:
            if lake[t] > 0:
                if gd > 0:
                    gd -= 1
                    ans += [t]

