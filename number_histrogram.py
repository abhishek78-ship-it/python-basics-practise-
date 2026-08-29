s = input()
n = int(input())
numbers = list(map(int, input().split()))

for x in numbers:
    print(s * x)
