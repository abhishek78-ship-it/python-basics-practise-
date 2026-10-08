# t = int(input())

# for _ in range(t):
#     n = int(input())
#     p = list(map(int, input().split()))

#     stack = []

#     for i in range(n):
#         x = i + 1

#         if p[i] > x:
#             stack.append(p[i])

#         elif p[i] < x:
#             if not stack or stack.pop() != p[i]:
#                 print("NO")
#                 break
#     else:
#         if not stack:
#             print("YES")
#         else:
#             print("NO")
t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    last = n + 1
    possible = True

    for i in range(n):
        pos = i + 1

        if p[i] != pos:
            if p[i] >= last:
                possible = False
                break

            last = p[i]

    print("YES" if possible else "NO")
