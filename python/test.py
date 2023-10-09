
def solution(s):
    list_a = list(map(int, s.split(' ')))
    answer = str(min(list_a)) + ' ' + str(max(list_a)) 

    return answer


s = "1 2 3 4"

print(solution(s))