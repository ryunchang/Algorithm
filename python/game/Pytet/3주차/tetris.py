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
	NewBlock, Running, Finished = range(3)

class tetris() :

    @classmethod
    def setOnLeftListener(cls, _myonLeft):
        tetris.myonLeft = _myonLeft
    @classmethod
    def setOnRightListener(cls, _myonRight):
        tetris.myonRight = _myonRight
    @classmethod
    def setOnDownListener(cls, _myonDown):
        tetris.myonDown = _myonDown
    @classmethod
    def setOnUpListener(cls, _myonUp):
        tetris.myonUp = _myonUp
    @classmethod
    def setOnDropListener(cls, _myonDrop):
        tetris.myonDrop = _myonDrop
    @classmethod
    def setOnCwListener(cls, _myonCw):
        tetris.myonCw = _myonCw
    @classmethod
    def setOnCcwListener(cls, _myonCcw):
        tetris.myonCcw = _myonCcw
    @classmethod
    def setOnNewBlockListener(cls, _myonNewBlock):
        tetris.myonNewBlock = _myonNewBlock
    @classmethod
    def setOnFinishedListener(cls, _myonFinished):
        tetris.myonFinished = _myonFinished
    @classmethod
    def setOperation(cls, key, op1, op2):
        temp = [op1, op2]
        tetris.operation_dic[key] = temp

    # Static variable
    nBlockTypes = len(arrayBlk) - 1

    # Dynamic variable
    def __init__(self ) :
        tetris.operation_dic = {}
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
        if key in tetris.operation_dic :
            if tetris.operation_dic.get(key)[0].run(self, key) :
                return tetris.operation_dic.get(key)[1].run(self, key)
            return TetrisState.Running
        else :
            print("Wrong Key!")

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

    def select_mode(self) :
        mode = int(input("Please select mode.\n\t0 : Game start\n\t1 : Add block\n\t2 : Set Dx, Dy\n>>"))
        if mode == 0 :
            self.renew_tempBlk()
            self.oScreen.paste(self.tempBlk, self.top, self.left)
            self.draw_matrix(self.oScreen); print()
            print(tetris.operation_dic)
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
        tetris.setOperation(str(tetris.nBlockTypes), tetris.myonNewBlock, tetris.myonFinished)   
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

    def count_score(self ) :
        self.score += 1
        print("Scored!!")
    
    def print_score(self ) :
        print("Your Score : " , self.score)

    def anyConflict(self):
        self.renew_tempBlk()
        if self.tempBlk.anyGreaterThan(1):
            return True

class base():
    def run(self, t, key) :
        raise NotImplementedError("Please Implement this method")
    
class onLeft(base) :
    def run(self, t, key):
        t.left -= 1
        return t.anyConflict()

class onRight(base) :
    def run(self, t, key):
        t.left += 1
        return t.anyConflict()

class onDown(base) :
    def run(self, t, key):
        t.top += 1
        return t.anyConflict()
    
class onUp(base) :
    def run(self, t, key):
        t.top -= 1
        t.renew_tempBlk()
        return TetrisState.NewBlock

class onDrop(base) :
    def run(self, t, key):
        while not t.tempBlk.anyGreaterThan(1) :
            tetris.myonDown.run(t, key)
            t.renew_tempBlk()
        return t.anyConflict()

class onCw(base) :
    def run(self, t, key):
        for k in range(0, len(t.currBlk.get_array())):
            for j in range(0, len(t.currBlk.get_array())):
                t.currBlk._array[j][len(t.currBlk.get_array())-1 - k] = t.tempCurrBlk._array[k][j] # 4x4 시계 회전 변환
        return t.anyConflict()

class onCcw(base) :
    def run(self, t, key):
        for k in range(0, len(t.currBlk.get_array())):
            for j in range(0, len(t.currBlk.get_array())):
                t.currBlk._array[len(t.currBlk.get_array())-1-k][j] = t.tempCurrBlk._array[j][k] # 4x4 반시계 회전 변환
        print("회전할 수 없는 위치입니다.")
        return t.anyConflict()
    
class onNewBlock(base) :
    def run(self, t, key):
        self.delete_line(t, key)
        t.currBlk = Matrix(arrayBlk[int(key)])
        t.iScreen = Matrix(t.oScreen)
        t.top = 0
        t.left = t.iScreenDw + t.iScreenDx//2 - 2
        t.renew_tempBlk() 
        return t.anyConflict()

    def delete_line(self, t, key) :
        fullLine = []
        for y in range(t.top, t.top+len( t.currBlk.get_array() )) :
            if all( t.oScreen._array[y] ) and y < t.iScreenDy :
                fullLine.append(y)         
        while fullLine:
            tempScreen = t.oScreen.clip(0, t.iScreenDw, fullLine.pop(0) , t.iScreenDx + t.iScreenDw)
            t.oScreen.paste(tempScreen, 1, t.iScreenDw)
            t.count_score()

class onFinished(base) :
    def run(self, t, key):
        print("OnFinished.run() called")
        return TetrisState.Finished


