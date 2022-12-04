# 파보나치 수열 x번째 수를 반환하는 함수
# 재귀함수로만 구현
import time

def fibo(x):
    if x==1 or x==2 :
        return 1
    return fibo(x-1) + fibo(x-2)

for i in range(5, 40, 10):
    start = time.time()
    res = fibo(i)
    print(res, "--> 러닝타임", round(time.time()-start,2))

print('')

# Dynamic Programming

d = [0] * 50
def fibo(x):
    if x==1 or x==2:
        d[1], d[2] = 1, 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

for i in range(5, 40, 10):
    start = time.time()
    res = fibo(i)
    print(res, "--> 러닝타임", round(time.time()-start,2))
