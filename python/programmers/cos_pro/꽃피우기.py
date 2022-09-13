def solution(garden):
    length = len(garden[0])
    day = 0
    while True:
        tmp = [[0 for _ in range(length)] for _ in range(length)]
        ggot = 0
        for jul in garden:
            if all(jul) : ggot = ggot + 1
        if ggot == length : return day
    
        day = day + 1
        for i in range(length):
            for j in range(length):
                if garden[i][j] == 1:
                    tmp[i][j] = 1
                    if i+1 < length : tmp[i+1][j] = 1
                    if j+1 < length : tmp[i][j+1] = 1
                    if i-1 >= 0 : tmp[i-1][j] = 1; 
                    if j-1 >= 0 : tmp[i][j-1] = 1
        garden = tmp

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
garden1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
ret1 = solution(garden1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

garden2 = [[1, 1], [1, 1]]
ret2 = solution(garden2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")
