from matrix import *
from random import randint

arrayBlk = [ [ [ 0, 0, 1, 0 ],
                [ 0, 0, 1, 0 ],
                [ 0, 0, 1, 0 ],
                [ 0, 0, 1, 0 ] ],   

              [ [ 0, 0, 1 ],
                [ 1, 1, 1 ],
                [ 0, 0, 0 ] ],   

              [ [ 0, 1, 0 ],
                [ 1, 1, 1 ],
                [ 0, 0, 0 ] ],   

              [ [ 1, 1 ],
                [ 1, 1 ] ], 

              [ [ 0, 1, 0 ],
                [ 0, 1, 1 ],
                [ 0, 0, 1 ] ],   

              [ [ 0, 1, 0 ],
                [ 1, 1, 0 ],
                [ 1, 0, 0 ] ],  

              [ [ 0, 0, 1 ],
                [ 1, 1, 1 ],
                [ 0, 0, 0 ] ] ]  

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

class TetrisState():
	Running, NewBlock, Finished = range(3)

class tetris() :

    # Static variable
    nBlockTypes = len(arrayBlk) - 1
    
    # Dynamic variable
    def __init__(self ) :
        self.iScreen = Matrix(arrayScreen)
        self.oScreen = Matrix(self.iScreen)
        self.iScreenDy = 15
        self.iScreenDx = 10
        self.iScreenDw = 4
        self.top = 0
        self.left = self.iScreenDw + self.iScreenDx//2 - 2
        self.score = 0
        self.state = 0
        self.currBlk = Matrix(arrayBlk[0])

    def accept(self, key) :
        if (key[0] == '0'): 
            self.currBlk = Matrix(arrayBlk[int(key[1])])
        else :
            self.input_key(key[0])
            self.renew_tempBlk()
            if self.check_collision(key[0]) :
                return TetrisState.NewBlock
        return TetrisState.Running

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
    
    def select_mode(self ) :
        mode = int(input("Please select mode.\n\t0 : Game start\n\t1 : Add block\n\t2 : Set Dx, Dy\n>>"))
        if mode == 0 :
            self.renew_tempBlk()
            self.oScreen.paste(self.tempBlk, self.top, self.left)
            self.draw_matrix(self.oScreen); print()
            return False
        elif mode == 1 :
            self.add_block()
        elif mode == 2 :
            self.set_xy()
        else :
            print("invalid value!!\n")
        return True

    def  add_block(self ) :
        size = int(input("Enter the size of the square matrix. : "))
        if size > self.iScreenDx :
            print("Should be less than x!!\n")
            return
        temp = [[0 for _ in range(size)] for _ in range(size)]  #initialize
        for y in range(0, size) :
            for x in range(0, size) :
                print("[",y,"], [",x,"] : ", end="")
                temp[y][x] = int(input())
        arrayBlk.append(temp)
        if self.iScreenDw < size :
            self.iScreenDw = size 
        tetris.nBlockTypes  += 1
        self.renew_oScreen()

    def set_xy(self ) :
        self.iScreenDx = int(input("Enter the size of the Dx :"))
        self.iScreenDy = int(input("Enter the size of the Dy :")) 
        self.renew_oScreen()
        print("Done!\n")

    def  renew_arrayScreen(self ) :
        del arrayScreen[:]

        wall_line = [1 for _ in range(0, self.iScreenDx + 2*self.iScreenDw) ]
        for x in range(self.iScreenDw, self.iScreenDw + self.iScreenDx) :
            wall_line[x] = 0
        ground_line = [1 for _ in range(0, 2 * self.iScreenDw + self.iScreenDx) ]

        for _ in range(0, self.iScreenDy) :
            arrayScreen.append(wall_line) 
        for _ in range(self.iScreenDy, self.iScreenDy+self.iScreenDw) :
            arrayScreen.append(ground_line)
        self.iScreen = Matrix(arrayScreen)
        self.oScreen = Matrix(self.iScreen)

    def renew_tempBlk(self ) :
        self.tempCurrBlk = Matrix(self.currBlk)
        self.tempBlk = self.iScreen.clip(self.top, self.left, self.top+self.currBlk.get_dy(), self.left+self.currBlk.get_dx())
        self.tempBlk = self.tempBlk + self.currBlk

    def renew_oScreen(self ) :
        self.renew_arrayScreen()
        self.top = 0
        self.left = self.iScreenDw + self.iScreenDx//2 - 2
        self.renew_tempBlk()
        self.oScreen.paste(self.tempBlk, self.top, self.left)

    def print_oScreen(self ) :
        self.print_score()
        self.oScreen = Matrix(self.iScreen)
        self.oScreen.paste(self.tempBlk, self.top, self.left)
        self.draw_matrix(self.oScreen); print()

    def input_key(self, key) :
        if key == 'q':
            print('Game terminated...')
            return 0
        elif key == 'a': # move self.left
            self.left -= 1
        elif key == 'd': # move right
            self.left += 1
        elif key == 's': # move down
            self.top += 1
        elif key == 'w': # rotate the block clockwise
            self.Rotate_Clockwise()
        elif key == ' ': # drop the block
            while not self.tempBlk.anyGreaterThan(1) :
                self.top += 1
                self.renew_tempBlk()
        else:
            print('Wrong key!!!')

    def check_collision(self, key) :
        if self.tempBlk.anyGreaterThan(1):
            if key == 'a': # undo: move right
                self.left += 1
            elif key == 'd': # undo: move self.left
                self.left -= 1
            elif key == 's': # undo: move up
                self.top -= 1
                self.renew_tempBlk()
                return True
            elif key == 'w': # undo: rotate the block counter-clockwise
                self.Rotate_CounterClockwise()
            elif key == ' ': # undo: move up
                self.top -= 1    # while문에서 검사를 위해 한칸 내린걸 다시 올려줌
                self.renew_tempBlk()
                return True
            self.renew_tempBlk()
            return False

    def Rotate_Clockwise(self):
        for k in range(0, len(self.currBlk.get_array())):
            for j in range(0, len(self.currBlk.get_array())):
                self.currBlk._array[j][len(self.currBlk.get_array())-1 - k] = self.tempCurrBlk._array[k][j] # 4x4 시계 회전 변환

    def Rotate_CounterClockwise(self):
        for k in range(0, len(self.currBlk.get_array())):
            for j in range(0, len(self.currBlk.get_array())):
                self.currBlk._array[len(self.currBlk.get_array())-1-k][j] = self.tempCurrBlk._array[j][k] # 4x4 반시계 회전 변환
        print("회전할 수 없는 위치입니다.")

    def delete_fullLine(self ) :
        fullLine = []
        for y in range(self.top, self.top+len( self.currBlk.get_array() )) :
            if all( self.oScreen._array[y] ) and y < self.iScreenDy :
                fullLine.append(y)         
        while fullLine:
            tempScreen = self.oScreen.clip(0, self.iScreenDw, fullLine.pop(0) , self.iScreenDx + self.iScreenDw)
            self.oScreen.paste(tempScreen, 1, self.iScreenDw)
            self.count_score()

    def make_newBlock(self ) :
        self.iScreen = Matrix(self.oScreen)
        self.top = 0
        self.left = self.iScreenDw + self.iScreenDx//2 - 2
        self.renew_tempBlk()
        if self.tempBlk.anyGreaterThan(1):
            self.state = TetrisState.Finished
            
    def count_score(self ) :
        self.score += 1
        print("Scored!!")
    
    def print_score(self ) :
        print("Your Score : " , self.score)
