s = input()

result = ""

for ch in s:
    if ch == ',':
        result += ' '
    elif ch.isupper():
        result += ch.lower()
    elif ch.islower():
        result += ch.upper()

print(result)
