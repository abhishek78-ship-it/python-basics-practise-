n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print("yes" if sorted(a) == sorted(b) else "no")
