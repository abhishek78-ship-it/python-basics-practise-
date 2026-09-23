n, m = map(int, input().split())

for _ in range(n):
    a = input().split()
    print(*reversed(a))
