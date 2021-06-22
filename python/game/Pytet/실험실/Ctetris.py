from tetris import *
import copy

class Ctetris(tetris) :
    def draw_matrix(self, m):
        array = m.get_array()
        for y in range(m.get_dy()):
            for x in range(m.get_dx()):
                if array[y][x] == 0:
                    print("□", end='')
                elif array[y][x] == 1:
                    print("■", end='')
                elif array[y][x] == 2 :
                    print("\x1b[92m" +"■"+"\x1b[0m", end='') #초록
                elif array[y][x] == 3 :
                    print("\x1b[31m" +"■"+"\x1b[0m", end='') #연노
                elif array[y][x] == 4 :
                    print("\x1b[94m" +"■"+"\x1b[0m", end='') #파랑
                elif array[y][x] == 5 :
                    print("\x1b[95m" +"■"+"\x1b[0m", end='') #보라
                elif array[y][x] == 6 :
                    print("\x1b[96m" +"■"+"\x1b[0m", end='') #하늘
                elif array[y][x] == 7 :
                    print("\x1b[33m" +"■"+"\x1b[0m", end='') #노랑
                elif array[y][x] == 8 :
                    print("\x1b[93m" +"■"+"\x1b[0m", end='') #빨강
                else:
                    print("\x1b[92m" +"■"+"\x1b[0m", end='') #초록
                    #print("XX", end='')
            print()

    def print_oScreen(self ) :
        self.print_score()
        self.oScreen = Matrix(self.iScreen)
        for _ in range(int(self.key)+2):
            self.tempBlk += self.currBlk
        self.oScreen.paste(self.tempBlk, self.top, self.left)
        self.draw_matrix(self.oScreen); print()

    def anyConflict(self):
        self.tempBlk = self.iScreen.clip(self.top, self.left, self.top+self.currBlk.get_dy(), self.left+self.currBlk.get_dx())
        temp_array = copy.deepcopy(self.tempBlk.get_array())
        for y in temp_array :
            for x in y:
                if x>1 :
                    su = int(x/x)
                    wit = y.index(x)
                    y.pop(wit)
                    y.insert(wit, su)
        temp_matrix = Matrix(temp_array)
        temp_matrix = temp_matrix + self.currBlk
        if temp_matrix.anyGreaterThan(1):
            return True

