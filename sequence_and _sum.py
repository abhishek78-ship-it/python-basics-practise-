while True:
    n, m = map(int, input().split())

    if n <= 0 or m <= 0:
        break

    if n > m:
        n, m = m, n

    total = 0

    for i in range(n, m + 1):
        print(i, end=" ")
        total += i

    print(f"sum ={total}")