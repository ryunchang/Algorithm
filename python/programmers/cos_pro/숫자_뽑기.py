
def solution(arr, K):
    l = len(arr)
    tmp = list()
    arr.sort()
    
    for i in range(l-K+1):
        tmp.append(arr[i+K-1]-arr[i])
            
    answer = min(tmp)
    return answer

arr = [9, 11, 9, 6, 4, 19]
K = 4
ret = solution(arr, K)

print("solution 함수의 반환 값은", ret, "입니다.")
