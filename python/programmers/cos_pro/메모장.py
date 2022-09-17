def solution(K, words):
    jul = ""
    n = 1
    for i in words:
        if len(jul)!=0 and len(jul+" "+i)>K:
            n = n + 1
            jul = i
        elif len(jul)==0:
            jul = i
        else :
            jul = jul + " " + i
            
    answer = n
    return answer

K = 10
words = ["nice", "happy", "hello", "world", "hi"]
ret = solution(10, words)

print("solution 함수의 반환 값은", ret, "입니다.")
