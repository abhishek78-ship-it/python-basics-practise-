A, B = map(int, input().split())

lucky = []

for num in range(A, B + 1):
    temp = str(num)

    is_lucky = True
    for digit in temp:
        if digit != '4' and digit != '7':
            is_lucky = False
            break

    if is_lucky:
        lucky.append(str(num))

if lucky:
    print(" ".join(lucky))
else:
    print(-1)