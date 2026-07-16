# n = int(input())

# a = n // 10
# b = n % 10

# if a % b == 0 or b % a == 0:
#     print("YES")
# else:
#     print("NO")
n = int(input())

a = n // 10
b = n % 10

if (a != 0 and b % a == 0) or (b != 0 and a % b == 0):
    print("YES")
else:
    print("NO")
