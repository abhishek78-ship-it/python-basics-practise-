n, k = map(int, input().split())
arr = list(map(int, input().split()))

ans = []

for i in range(0, n, k):
    minimum = arr[i]
    end = min(i + k, n)

    for j in range(i + 1, end):
        if arr[j] < minimum:
            minimum = arr[j]

    ans.append(str(minimum))

print(" ".join(ans))