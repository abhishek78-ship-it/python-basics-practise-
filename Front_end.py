n = int(input())
a = list(map(int, input().split()))

ans = []

left = 0
right = n - 1

while left <= right:
    ans.append(a[left])
    left += 1

    if left <= right:
        ans.append(a[right])
        right -= 1

print(*ans)
