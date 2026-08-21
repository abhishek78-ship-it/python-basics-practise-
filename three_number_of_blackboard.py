t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    nums = sorted([a, b, c])
    if nums[2] > nums[0] + nums[1]:
        nums[2] = nums[0] + nums[1]
    print(nums[2] - nums[0])