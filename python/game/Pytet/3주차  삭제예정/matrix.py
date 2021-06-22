class MatrixError(Exception):
    pass

class Matrix:
    nAlloc = 0
    nFree = 0

    def get_nAlloc(self):
        return Matrix.nAlloc

    def get_nFree(self):
        return Matrix.nFree
    
    def get_dy(self):
        return self._dy

    def get_dx(self):
        return self._dx

    def get_array(self):
        return self._array

    def __del__(self):
        Matrix.nFree += 1

    def __alloc(self, cy, cx):  # _dy, _dx, _array 할당을 위한 함수
        if cy < 0 or cx < 0:    # Special Case
            raise MatrixError("wrong matrix size")
        self._dy = cy   # 객체 변수로 가로줄, 세로줄 추가
        self._dx = cx
        self._array = [[0]*self._dx for i in range(self._dy)]   # 컴프리헨션
        #print(self.__array)
        Matrix.nAlloc += 1
        
    def __init__(self, arg):
        if isinstance(arg, list): #List이면
            array = arg
            cy = len(array)     # 세로줄 수
            cx = len(array[0])  # 가로줄 수
            self.__alloc(cy, cx)
            for y in range(cy):
                for x in range(cx):
                    self._array[y][x] = array[y][x]     #할당된 _array는 0이므로 다시 재정의
            return
        elif isinstance(arg, Matrix):   # class Matrix형 이면
            other = arg
            cy = other._dy  # Matrix형 변수이므로 _dy, _dx를 바로 대입
            cx = other._dx
            self.__alloc(cy, cx)
            for y in range(cy):
                for x in range(cx):
                    self._array[y][x] = other._array[y][x]
            return
        else:
            self.__alloc(0, 0)
            return

    def __str__(self):
        return 'Matrix(%d, %d)' % (self._dy, self._dx)


    def print(self):
        print('[', end=' ')
        for y in range(self._dy-1):
            print('[', end=' ')
            for x in range(self._dx-1):
                print(self._array[y][x], end=', ')
            print(self._array[y][self._dx-1], end=' ')
            print('],', end=' ')
        print('[', end=' ')
        for x in range(self._dx-1):
            print(self._array[self._dy-1][x], end=', ')
        print(self._array[self._dy-1][self._dx-1], end=' ')
        print(']', end=' ')
        print(']')        


    def clip(self, top, left, bottom, right):   # top, left, bottom, right 의 행렬만 잘라서 반환
        cy = bottom - top
        cx = right - left
        temp = [[0]*cx for i in range(cy)]       
        for y in range(cy):
            for x in range(cx):
                if (top+y >= 0) and (left+x >= 0) \
                   and (top+y < self._dy) and (left+x < self._dx):
                    temp[y][x] = self._array[top+y][left+x]
                else:
                    raise MatrixError("invalid matrix range")
        return Matrix(temp)

    def paste(self, other, top, left):  # 붙혀넣는 함수 (top, left는 붙혀놓기 시작할 위치)
        for y in range(other._dy):
            for x in range(other._dx):
                if (top+y >= 0) and (left+x >= 0) \
                   and (top+y < self._dy) and (left+x < self._dx):
                    self._array[top+y][left+x] = other._array[y][x]
                else:
                    raise MatrixError("invalid matrix range")


    def __add__(self, other):       # 행렬이 같은 배열 각 자리 더하는 매서드
        if (self._dx != other._dx) or (self._dy != other._dy):
            raise MatrixError("matrix sizes mismatch")
        temp = [[0]*self._dx for i in range(self._dy)]
        for y in range(self._dy):
            for x in range(self._dx):
                temp[y][x] = self._array[y][x] + other._array[y][x]                
        return Matrix(temp)

    def sum(self):
        total = 0
        for y in range(self._dy):
            for x in range(self._dx):
                total += self._array[y][x]
        return total

    def mulc(self, coef):
        for y in range(self._dy):
            for x in range(self._dx):
                self._array[y][x] *= coef

    def anyGreaterThan(self, val):  # 행렬 중 1보다 큰게 있으면 겹치는게 있으므로 False 반환
        for y in range(self._dy):
            temp = [v for v in self._array[y] if v > val]
            if len(temp) > 0:
                return True
        return False



