from collections import deque

n = int(input())
a = list(map(int, input().split()))

ans = deque()

for x in a:
    if x == 0:
        ans.reverse()
    ans.append(x)

print(*ans)
