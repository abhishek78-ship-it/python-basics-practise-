# t = int(input())

# for _ in range(t):
#     n, k = map(int, input().split())

#     ans = 0
#     money = 1

#     for day in range(1, n + 1):

#         money *= 2

#         if k > 0:
#             ans += money
#             money = 1
#             k -= 1

#     print(ans)
# t = int(input())
# for _ in range(t):
#     n, k = map(int, input().split())
#     ans = 0
#     for i in range(k):
#         days = n - k + i + 1
#         ans += 2 ** days

#     print(ans)
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    ans = (2 ** (n - k + 1)) + (2 * (k - 1))

    print(ans)
