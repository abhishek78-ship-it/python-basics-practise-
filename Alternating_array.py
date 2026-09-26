n = int(input())
a = list(map(int, input().split()))

pos = 0  
neg = 0  

for i in range(n):
    if i % 2 == 0:
       
        if a[i] < 0:
            pos += 1

      
        if a[i] > 0:
            neg += 1
    else:
      
        if a[i] > 0:
            pos += 1

      
        if a[i] < 0:
            neg += 1

print(min(pos, neg))
