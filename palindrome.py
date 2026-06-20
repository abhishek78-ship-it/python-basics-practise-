n = int(input())

temp = n
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

print(rev)

if n == rev:
    print("YES")
else:
    print("NO")