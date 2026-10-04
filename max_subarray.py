t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ans = []

    for i in range(n):
        mx = a[i]

        for j in range(i, n):
            mx = max(mx, a[j])
            ans.append(mx)

    print(*ans)
