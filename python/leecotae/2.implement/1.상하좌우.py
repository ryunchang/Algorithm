size = int(input())
move = list(input().split())

array = [[1]*size for _ in range(size)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

x, y = 0, 0

while move:
    direct = move.pop(0)
    if direct == "R":
        x = x + dx[0]
        y = y + dy[0]
        if not ((0 <= x < size) and (0 <= y < size)):
            x = x + dx[1]
            y = y + dy[1]
    elif direct == "L":
        x = x + dx[1]
        y = y + dy[1]
        if not ((0 <= x < size) and (0 <= y < size)):
            x = x + dx[0]
            y = y + dy[0]
    elif direct == "D":
        x = x + dx[2]
        y = y + dy[2]
        if not ((0 <= x < size) and (0 <= y < size)):
            x = x + dx[3]
            y = y + dy[3]
    elif direct == "U":
        x = x + dx[3]
        y = y + dy[3]
        print(x, y)
        print(array[x][y])
        if not ((0 <= x < size) and (0 <= y < size)):
            x = x + dx[2]
            y = y + dy[2]
    else :
        pass


print("[" + str(y+1) + ", " + str(x+1) + "]")
