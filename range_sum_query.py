n, q = map(int, input().split())

a = list(map(int, input().split()))
prefix = [0] * (n + 1)

for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + a[i - 1]
for i in range(q):
    l, r = map(int, input().split())

    ans = prefix[r] - prefix[l - 1]

    print(ans)
