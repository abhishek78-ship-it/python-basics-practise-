id = int(input())

row = id // 4
rem = id % 4

if row % 2 == 0:
    col = rem
else:
    col = 3 - rem

print(row, col)