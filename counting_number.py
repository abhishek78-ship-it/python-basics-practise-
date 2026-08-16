n = int(input())
a = list(map(int, input().split()))
s = set(a)
count = 0
for x in a:
    if x + 1 in s:
        count += 1
print(count)