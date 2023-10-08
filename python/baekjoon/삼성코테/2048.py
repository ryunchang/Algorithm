# 2048문제 - BFS
from collections import deque

MOVE_COUNT = 5
CASE_OF_DIRECTION = 4

N = int(input())

board = list()
for i in range(N):
    tmp = input().split(" ")
    board.append(tmp)


Queue = deque()
cnt = 0

def move_all_direction(current_board):
    move_top_direction(current_board)
    move_bottom_direction(current_board)
    move_left_direction(current_board)
    move_right_direction(current_board)

def move_top_direction(current_board):
    for i in range(1, N):
        for j in range(N):
            di = i - 1
            while(di>=0 and current_board[di,j]==0):
                di -= 1  
            if current_board[i,j] == current_board[di,j]:
                current_board[di,j] = 2*current_board[i,j]




while not(cnt == MOVE_COUNT):  # 5회가 될 때까지 반복
    
    for i in range(CASE_OF_DIRECTION):
        
        move_all_direction(current_board)
    cnt += 1


    




