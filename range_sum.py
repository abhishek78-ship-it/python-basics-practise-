t = int(input())

for _ in range(t):
    l, r = map(int, input().split())

    if l > r:
        l, r = r, l

    ans = r * (r + 1) // 2 - (l - 1) * l // 2
    print(ans)