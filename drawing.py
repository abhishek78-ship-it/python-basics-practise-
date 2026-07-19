n = int(input())

for i in range(n):
    for j in range(n):
        if i == n // 2 and j == n // 2:
            print("X", end="")
        elif i == j:
            print("\\", end="")
        elif i + j == n - 1:
            print("/", end="")
        else:
            print("*", end="")
    print()