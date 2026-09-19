n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse=True)

ans = 0

for i in range(k):
    if a[i] > 0:
        ans += a[i]

print(ans)
