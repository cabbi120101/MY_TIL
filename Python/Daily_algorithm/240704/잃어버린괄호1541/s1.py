s1 = input()
s1 = s1.split('-')
ans = sum(map(int,s1[0].split('+'))) 
for i in s1[1:]:
    ans -= sum(map(int,i.split('+')))
print(ans)