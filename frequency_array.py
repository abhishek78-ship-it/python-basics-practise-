n, m = map(int, input().split())
a = list(map(int, input().split()))
freq = [0] * (m + 1)
for x in a:
    freq[x] += 1

for i in range(1, m + 1):
    print(freq[i])
