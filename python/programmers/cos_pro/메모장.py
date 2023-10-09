def solution(K, words):
    
    jul = ""
    n = 0
    for word in words:
        if len(jul) == 0 :
            jul = word
            n += 1
        elif len(jul + " " + word) > 10:
            jul = word
            n += 1
        else:
            jul = jul + ' ' + word
    answer = n
    return answer

K = 10
words = ["nice", "happy", "hello", "world", "hi"]
ret = solution(10, words)

print("solution 함수의 반환 값은", ret, "입니다.")
