T = int(input())

for _ in range(T):
    N = int(input())
    ones = N.bit_count()
    answer = (1 << ones) - 1
    print(answer)
