import time

n, k = map(int, input().split())

result = 0

start = time.time()
while True:
    
    target = (n//k) * k
    result += (n-target)
    n = target

    if n < k:
        break

    result += 1
    n //= k
result += (n-1)
end = time.time()

print(end-start)
print(result)

