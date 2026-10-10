a = input()
b = input()

print(len(a), len(b))
print(a + b)

x = a[0]
y = b[0]

a = y + a[1:]
b = x + b[1:]

print(a, b)
