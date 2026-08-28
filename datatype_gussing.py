n, k, a = map(int, input().split())

product = n * k

if product % a != 0:
    print("double")
else:
    result = product // a

    if result <= 2147483647:
        print("int")
    elif result <= 9223372036854775807:
        print("long long")
    else:
        print("double")
