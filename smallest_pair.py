t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ans = 10**18
    min_value = a[0] - 1

    for j in range(1, n):
        current = min_value + a[j] + (j + 1)
        ans = min(ans, current)

        min_value = min(min_value, a[j] - (j + 1))

    print(ans)
