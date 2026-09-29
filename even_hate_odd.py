t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if n % 2 != 0:
        print(-1)
        continue

    even = 0
    odd = 0

    for x in a:
        if x % 2 == 0:
            even += 1
        else:
            odd += 1

    ans = abs(even - odd) // 2

    print(ans)
