t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if n % 2 == 0 and a.count(-1) % 2 == (n // 2) % 2:
        print("YES")
    else:
        print("NO")