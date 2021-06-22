from matrix import *
from random import randint

def draw_matrix(m):
    array = m.get_array()
    for y in range(m.get_dy()):
        for x in range(m.get_dx()):
            if array[y][x] == 0:
                print("□", end='')
            elif array[y][x] == 1:
                print("■", end='')
            else:
                print("XX", end='')
        print()


###
### initialize variables
###     
arrayBlk = [ [ [ 0, 0, 1, 0 ],
                [ 0, 0, 1, 0 ],
                [ 0, 0, 1, 0 ],
                [ 0, 0, 1, 0 ] ],   # |

              [ [ 0, 0, 1 ],
                [ 1, 1, 1 ],
                [ 0, 0, 0 ] ],   # ㄴ

              [ [ 0, 1, 0 ],
                [ 1, 1, 1 ],
                [ 0, 0, 0 ] ],   # ㅗ

              [ [ 1, 1 ],
                [ 1, 1 ] ],  # ㅁ

              [ [ 0, 1, 0 ],
                [ 0, 1, 1 ],
                [ 0, 0, 1 ] ],   # 번개모양

              [ [ 0, 1, 0 ],
                [ 1, 1, 0 ],
                [ 1, 0, 0 ] ],   # 좌우 반전 번개모양

              [ [ 0, 0, 1 ],
                [ 1, 1, 1 ],
                [ 0, 0, 0 ] ] ]  # ┛

### integer variables: must always be integer!
iScreenDy = 15
iScreenDx = 10
iScreenDw = 4
top = 0
left = iScreenDw + iScreenDx//2 - 2

newBlockNeeded = False

arrayScreen = [
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] ]

###
### prepare the initial screen output
###  
iScreen = Matrix(arrayScreen)
oScreen = Matrix(iScreen)
random_int = randint(0,len(arrayBlk)-1)
currBlk = Matrix(arrayBlk[random_int])
tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
tempBlk = tempBlk + currBlk
tempCurrBlk = Matrix(currBlk)
oScreen.paste(tempBlk, top, left)
draw_matrix(oScreen); print()

###
### execute the loop
###

while True:
    key = input('Enter a key from [ q (quit), a (left), d (right), s (down), w (rotate), \' \' (drop) ] : ')
    if key == 'q':
        print('Game terminated...')
        break
    elif key == 'a': # move left
        left -= 1
    elif key == 'd': # move right
        left += 1
    elif key == 's': # move down
        top += 1
    elif key == 'w': # rotate the block clockwise
        for k in range(0, len(currBlk.get_array())):
            for j in range(0, len(currBlk.get_array())):
                currBlk._array[j][len(currBlk.get_array())-1 - k] = tempCurrBlk._array[k][j] # 4x4 회전 변환
    elif key == ' ': # drop the block
        while not tempBlk.anyGreaterThan(1) :
            top += 1
            tempBlk = iScreen.clip(top, left, top + currBlk.get_dy(), left + currBlk.get_dx())
            tempBlk = tempBlk + currBlk
    else:
        print('Wrong key!!!')
        continue

    tempCurrBlk = Matrix(currBlk)   # tempCurr 블럭 최신화
    tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
    tempBlk = tempBlk + currBlk

    if tempBlk.anyGreaterThan(1):
        if key == 'a': # undo: move right
            left += 1
        elif key == 'd': # undo: move left
            left -= 1
        elif key == 's': # undo: move up
            top -= 1
            newBlockNeeded = True
        elif key == 'w': # undo: rotate the block counter-clockwise
            for k in range(0, len(currBlk.get_array())):
                for j in range(0, len(currBlk.get_array())):
                    currBlk._array[len(currBlk.get_array())-1-k][j] = tempCurrBlk._array[j][k]
            print("회전할 수 없는 위치입니다.")
        elif key == ' ': # undo: move up
            top -= 1    # while문에서 검사를 위해 한칸 내린걸 다시 올려줌
            newBlockNeeded = True

        tempCurrBlk = Matrix(currBlk)
        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk

    oScreen = Matrix(iScreen)
    oScreen.paste(tempBlk, top, left)
    draw_matrix(oScreen); print()

    if newBlockNeeded:

        fullLine = []
        for y in range(top, top+len( currBlk.get_array() )) :
            if all( oScreen._array[y] ) and y < iScreenDy :
                fullLine.append(y)
                
        while fullLine:
            tempScreen = oScreen.clip(0, iScreenDw, fullLine.pop(0) , iScreenDx + iScreenDw)
            oScreen.paste(tempScreen, 1, iScreenDw)

        iScreen = Matrix(oScreen)
        top = 0
        left = iScreenDw + iScreenDx//2 - 2
        newBlockNeeded = False
        currBlk = Matrix(arrayBlk[randint(0,6)])
        tempCurrBlk = Matrix(currBlk)               # 새로운 블럭 tempCurrBlk 최신화
        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk

        if tempBlk.anyGreaterThan(1):
            print('Game Over!!!')
            break
        
        oScreen = Matrix(iScreen)
        oScreen.paste(tempBlk, top, left)
        draw_matrix(oScreen); print()
        
###
### end of the loop
###
