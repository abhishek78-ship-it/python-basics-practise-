n = int(input())
arr = list(map(int, input().split()))

minimum = arr[0]
position = 1

for i in range(1, n):
    if arr[i] < minimum:
        minimum = arr[i]
        position = i + 1  # 1-based indexing

print(minimum, position)