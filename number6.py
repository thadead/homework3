n=int(input())
N = n // 2
t = 1
count = 0
while t <= N:
    t *= 2
    count += 1
print(count, t)