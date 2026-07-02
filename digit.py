t = int(input())

for _ in range(t):
    n = int(input())

    if n == 0:
        print(0)
    else:
        while n > 0:
            print(n % 10, end=" ")
            n //= 10
        print()