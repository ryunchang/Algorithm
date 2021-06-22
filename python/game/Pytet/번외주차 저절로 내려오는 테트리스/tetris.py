from matrix import *
from random import randint
import time
import msvcrt

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
                [ 0, 1, 1 ],
                [ 0, 0, 1 ] ],   # 좌우 반전 번개모양

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


class tetris :
    def __init__ (self) :
        self.score = 0
        self.iScreen = Matrix(arrayScreen)
        self.oScreen = Matrix(self.iScreen)
        self.currBlk = Matrix(arrayBlk[randint(0,6)])
        self.tempBlk = self.iScreen.clip(top, left, top+self.currBlk.get_dy(), left+self.currBlk.get_dx())
        self.tempBlk = self.tempBlk + self.currBlk
        self.tempCurrBlk = Matrix(self.currBlk)
        self.oScreen.paste(self.tempBlk, top, left)
        self.draw_matrix(self.oScreen); print()

    def draw_matrix(self, m):
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
    
    def print_screen(self):
        self.oScreen = Matrix(self.iScreen)
        self.oScreen.paste(self.tempBlk, top, left)
        self.draw_matrix(self.oScreen);
        print("score : ", self.score)

    def is_game_over(self):
        if self.tempBlk.anyGreaterThan(1):
            print('Game Over!!!')
            return True
        return False

    def erase_line(self):
        fullLine = [y for y in range(top, top+len(self.currBlk.get_array())) if all(self.oScreen._array[y]) and (y < iScreenDy)]
        while fullLine:
            self.iScreen = Matrix(self.oScreen)
            delLine = fullLine.pop(0)
            self.score += 1
            tempScreen = self.iScreen.clip(0, iScreenDw, delLine , iScreenDx + iScreenDw+1)
            self.oScreen = Matrix(self.iScreen)
            self.oScreen.paste(tempScreen, 1, iScreenDw)

    def made_tempBlk(self):
        self.tempCurrBlk = Matrix(self.currBlk)   # tempCurr 블럭 최신화
        self.tempBlk = self.iScreen.clip(top, left, top+self.currBlk.get_dy(), left+self.currBlk.get_dx())
        self.tempBlk = self.tempBlk + self.currBlk

    def Rotate_Clockwise(self):
        for k in range(0, len(self.currBlk.get_array())):
            for j in range(0, len(self.currBlk.get_array())):
                self.currBlk._array[j][len(self.currBlk.get_array())-1 - k] = self.tempCurrBlk._array[k][j] # 4x4 시계 회전 변환

    def Rotate_CounterClockwise(self):
        for k in range(0, len(self.currBlk.get_array())):
            for j in range(0, len(self.currBlk.get_array())):
                self.currBlk._array[len(self.currBlk.get_array())-1-k][j] = self.tempCurrBlk._array[j][k] # 4x4 반시계 회전 변환
        print("회전할 수 없는 위치입니다.")
    
    def main(self):
        global left, top, newBlockNeeded
        while True:
            key = 's'
            if msvcrt.kbhit() :
                key = msvcrt.getwch()
            #key = input('Enter a key from [ q (quit), a (left), d (right), s (down), w (rotate), \' \' (drop) ] : ')
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
                self.Rotate_Clockwise()
            elif key == ' ': # drop the block
                while not self.tempBlk.anyGreaterThan(1) :
                    top += 1
                    self.made_tempBlk()
            # else:
            #     print('Wrong key!!!')
            #     continue

            self.made_tempBlk()

            if self.tempBlk.anyGreaterThan(1):
                if key == 'a': # undo: move right
                    left += 1
                elif key == 'd': # undo: move left
                    left -= 1
                elif key == 's': # undo: move up
                    top -= 1
                    newBlockNeeded = True
                elif key == 'w': # undo: rotate the block counter-clockwise
                    self.Rotate_CounterClockwise()
                elif key == ' ': # undo: move up
                    top -= 1    # while문에서 검사를 위해 한칸 내린걸 다시 올려줌
                    newBlockNeeded = True
                self.made_tempBlk()
                
            self.print_screen()

            if newBlockNeeded:
                self.erase_line()
                self.iScreen = Matrix(self.oScreen)
                top = 0
                left = iScreenDw + iScreenDx//2 - 2
                newBlockNeeded = False
                self.currBlk = Matrix(arrayBlk[randint(0,6)])
                self.made_tempBlk()
                if self.is_game_over():
                    break
                self.print_screen()
            time.sleep(0.2)


a = tetris()
a.main()

print("\n\nYou scored : ", a.score); 
temp = input("\n아무 키를 눌러 종료....")
