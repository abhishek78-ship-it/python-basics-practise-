n = int(input())
arr = list(map(int, input().split()))

ans = 0

for x in arr:
    count = 0
    while x % 2 == 0:
        count += 1
        x //= 2
    if count > ans:
        ans = count

print(ans)