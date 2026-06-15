n = int(input())
numbers = list(map(int, input().split()))

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print(maximum)