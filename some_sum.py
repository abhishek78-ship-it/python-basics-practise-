N, A, B = map(int, input().split())
ans = 0
for i in range(1, N + 1):
    digit_sum = 0
    num = i
    while num > 0:
        digit_sum += num % 10
        num //= 10
    if A <= digit_sum <= B:
        ans += i
print(ans)