# 2048문제 - BFS
from collections import deque

MOVE_COUNT = 5
CASE_OF_DIRECTION = 4

N = int(input())

board = list()
for i in range(N):
    tmp = list(map(int, input().split(" ")))
    board.append(tmp)


Queue = deque()
cnt = 0

# def move_all_direction(current_board):
#     move_top_direction(current_board)
#     move_bottom_direction(current_board)
#     move_left_direction(current_board)
#     move_right_direction(current_board)

def move_top_direction(current_board):
    check_list = [[True for _ in range(N)] for _ in range(N)]
    print(check_list)
    for i in range(1, N):
        for j in range(N):
            if current_board[i][j]:
                di = i
                while (di-1>=0 and current_board[di-1][j]==0):
                    di -= 1
                    print(di)

                if (current_board[i][j] == current_board[di][j]) and (check_list[di][j]): # 숫자 같고 합쳐진적 없으면 합치기
                    current_board[di][j] = 2*int(current_board[i][j])
                    current_board[i][j] = 0  # 원래 있던 자리 빈공간 만들기
                    check_list[di][j] = False
                elif (current_board[di][j]==0):
                    current_board[di][j] = current_board[i][j]
                    current_board[i][j] = 0  # 원래 있던 자리 빈공간 만들기  
                else :
                    current_board[di+1][j] = current_board[i][j]
                    current_board[i][j] = 0  # 원래 있던 자리 빈공간 만들기
        print(current_board)
    return current_board


print(move_top_direction(board))    


# while not(cnt == MOVE_COUNT):  # 5회가 될 때까지 반복
            
#     move_all_direction(current_board)
#     cnt += 1


    




