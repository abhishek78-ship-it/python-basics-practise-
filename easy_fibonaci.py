# n= int(input("Enter a number: "))
# a, b = 0, 1
# for i in range(n):
#    print(a, end=' ')
#    a, b = b, a + b
#  failed error

# def fib(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     return fib(n - 1) + fib(n - 2)

# n = int(input())

# for i in range(1, n + 1):
#     print(fib(i), end=" ")
# time limit exceed error

n = int(input())

fib = [0, 1]

for i in range(2, n):
    fib.append(fib[i - 1] + fib[i - 2])

print(*fib[:n])
