n = int(input())
arr = list(map(int, input().split()))
mn = min(arr)
mx = max(arr)
min = arr.index(mn)
max = arr.index(mx)
arr[min], arr[max] = arr[max], arr[min]
print(*arr)