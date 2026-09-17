K, S = map(int, input().split())
 
def C2(n):
    return n * (n - 1) // 2 if n >= 2 else 0
 
ans = C2(S + 2)
ans -= 3 * C2(S - K + 1)
ans += 3 * C2(S - 2 * K)
ans -= C2(S - 3 * K - 1)
 
print(ans)
