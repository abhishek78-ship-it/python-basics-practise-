A, B = map(int, input().split())
S = input()
if len(S) != A + B + 1:
    print("No")
else:
    valid = True
    for i in range(len(S)):
        if i == A:
            if S[i] != '-':
                valid = False
                break
        else:
            if not S[i].isdigit():
                valid = False
                break
    print("Yes" if valid else "No")