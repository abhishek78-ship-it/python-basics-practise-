t = int(input())

for _ in range(t):
    n, s = map(int, input().split())

    max_sum = n * (n + 1) // 2

    if s > max_sum:
        print(-1)
        continue

    ans = []

    for i in range(n, 0, -1):
        if s >= i:
            ans.append(i)
            s -= i
        if s == 0:
            break

    print(*ans)