INC = 0
DEC = 1

def func_a(arr): # 가장 긴 것의 길이를 담은 리스트 생성 수
    length = len(arr)
    ret = [0 for _ in range(length)]
    ret[0] = 1
    for i in range(1, length):
        if arr[i] != arr[i-1]: # 그 전 숫자와 같지 않다면
            ret[i] = ret[i-1] + 1 # 1을 증가하고 
        else:
            ret[i] = 2  # 아니면 2를 넣음
    return ret

def func_b(arr):  
    global INC, DEC
    length = len(arr)
    ret = [0 for _ in range(length)]
    ret[0] = -1
    for i in range(1, length):  
        if arr[i] > arr[i-1]:  # 그 전 숫자보다 크다면
            ret[i] = INC
        elif arr[i] < arr[i-1]:  # 작다면
            ret[i] = DEC 
    return ret

def func_c(arr):
    ret = max(arr)
    if ret == 2:
        return 0
    return ret

def solution(S):
    check = func_b(S)
    dp = func_a(check)
    answer = func_c(dp)
    return answer


S1 = [2, 5, 7, 3, 4, 6, 1, 8, 9]
ret1 = solution(S1)

print("solution 함수의 반환 값은", ret1, "입니다.")

S2 = [4, 3, 2, 1, 10, 6, 9, 7, 8]
ret2 = solution(S2)

print("solution 함수의 반환 값은", ret2, "입니다.")

S3 = [1, 2, 3, 4, 5]
ret3 = solution(S3)

print("solution 함수의 반환 값은", ret3, "입니다.")
