import time

N, K = map(int, input().split())
cnt = 0

start = time.time()
while(N != 1):
    if( N % K != 0):
        N -= 1
        cnt += 1
    else:
        N /= K
        cnt += 1
end = time.time()

print(end-start)
print(cnt)
