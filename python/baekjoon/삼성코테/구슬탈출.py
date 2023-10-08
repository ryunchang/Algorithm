N, M = map(int, input().split(" "))

pan = []
for i in range(N):
    tmp = input()
    pan.append(list(tmp))

dx = [1, 0, -1, 0]  # 우, 하, 좌, 상
dy = [0, 1, 0, -1]

from collections import deque
import copy

def bfs(pan, N, M):
    count = 0
    queue = deque()
    queue.append([count, pan])
    
    while queue:
        count, a = queue.popleft()
        count += 1

        for i, row in enumerate(a) :
            if "B" in row :  B_pos = [i, row.index("B")]
            if "R" in row :  R_pos = [i, row.index("R")]
        print(B_pos, R_pos)

        def move(board, n_pos, i):
            color = board[n_pos[0]][n_pos[1]]
            print(color)
            board[n_pos[0]][n_pos[1]] = '.'
            while True :
                n_pos[1] += dx[i]
                n_pos[0] += dy[i] 
                if board[n_pos[0]][n_pos[1]] == ".": continue 
                elif board[n_pos[0]][n_pos[1]] == 'O' and color == "B": return -1, board
                elif board[n_pos[0]][n_pos[1]] == 'O' and color == "R": return 1, board
                elif board[n_pos[0]][n_pos[1]] == "#" or board[n_pos[0]][n_pos[1]] == "R" or board[n_pos[0]][n_pos[1]] == "B":  
                    board[n_pos[0]-dy[i]][n_pos[1]-dx[i]] = color  # back one shot and put color
                    return 0, board
                else: return 0, board

        for i in range(4):
            a_copy = copy.deepcopy(a)
            B_pos_copy = copy.deepcopy(B_pos)
            R_pos_copy = copy.deepcopy(R_pos)

            if dx[i] == 1 and dy[i] == 0 : # right
                if B_pos_copy[1] > R_pos_copy[1]: # blue first
                    res, tmp = move(a_copy, B_pos_copy, i)
                    res, tmp = move(tmp, R_pos_copy, i)  
                    if res==1: return count
                    elif res==-1: pass
                    elif tmp == a: pass
                    else: queue.append([count, tmp])
                else: 
                    res, tmp = move(a_copy, R_pos_copy, i)
                    res, tmp = move(tmp, B_pos_copy, i) 
                    if res==1: return count
                    elif res==-1: pass
                    elif tmp == a: pass
                    else: queue.append([count, tmp])
                print("right")
                print(tmp)
                print(res)

            elif dx[i] == 0 and dy[i] == 1 : # down
                if B_pos_copy[0] > R_pos_copy[0]: # blue first
                    res, tmp = move(a_copy, B_pos_copy, i)  
                    res, tmp = move(tmp, R_pos_copy, i) 
                    if res==1: return count
                    elif res==-1: pass
                    elif tmp == a: pass
                    else: queue.append([count, tmp])
                else: 
                    res, tmp = move(a_copy, R_pos_copy, i)
                    res, tmp = move(tmp, B_pos_copy, i)
                    if res==1: return count
                    elif res==-1: pass
                    elif tmp == a: pass
                    else: queue.append([count, tmp])
                print("down")
                print(tmp)
                print(res)

            elif dx[i] == -1 and dy[i] == 0 : # left
                if B_pos_copy[1] < R_pos_copy[1]: # blue first
                    res, tmp = move(a_copy, B_pos_copy, i)
                    res, tmp = move(tmp, R_pos_copy, i) 
                    if res==1: return count
                    elif res==-1: pass
                    elif tmp == a: pass
                    else: queue.append([count, tmp])
                else: 
                    res, tmp = move(a_copy, R_pos_copy, i)
                    res, tmp = move(tmp, B_pos_copy, i) 
                    if res==1: return count
                    elif res==-1: pass
                    elif tmp == a: pass
                    else: queue.append([count, tmp])
                print("left")
                print(tmp)
                print(res)

            elif dx[i] == 0 and dy[i] == -1 : # up
                if B_pos_copy[0] < R_pos_copy[0]: # blue first
                    res, tmp = move(a_copy, B_pos_copy, i)
                    res, tmp = move(tmp, R_pos_copy, i) 
                    if res==1: return count
                    elif res==-1: pass
                    elif tmp == a: pass
                    else: queue.append([count, tmp])
                else: 
                    res, tmp = move(a_copy, R_pos_copy, i)
                    res, tmp = move(tmp, B_pos_copy, i)
                    if res==1: return count
                    elif res==-1: pass
                    elif tmp == a: pass
                    else: queue.append([count, tmp])
                print("up")
                print(tmp)
                print(res)



print( bfs(pan, N, M) )