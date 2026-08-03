n = int(input())
arr = list(map(int, input().split()))

minimum = min(arr)
count = arr.count(minimum)

if count % 2 == 1:
    print("Lucky")
else:
    print("Unlucky")