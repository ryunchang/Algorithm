from matrix import *
from tetris import *
import os


def main() :
    a = tetris() 

    myonLeft = onLeft()
    myonRight = onRight()
    myonDown = onDown()
    myonUp = onUp()
    myonDrop = onDrop()
    myonCw = onCw()
    myonCcw = onCcw()
    myonNewBlock = onNewBlock()
    myonFinished = onFinished()

    tetris.setOnLeftListener(myonLeft)
    tetris.setOnRightListener(myonRight)
    tetris.setOnDownListener(myonDown)
    tetris.setOnUpListener(myonUp)
    tetris.setOnCwListener(myonCw)
    tetris.setOnCcwListener(myonCcw)
    tetris.setOnDropListener(myonDrop)
    tetris.setOnNewBlockListener(myonNewBlock)
    tetris.setOnFinishedListener(myonFinished)
    
    tetris.setOperation('q', myonFinished, myonFinished)
    tetris.setOperation('a', myonLeft, myonRight)
    tetris.setOperation('d', myonRight, myonLeft)
    tetris.setOperation('s', myonDown, myonUp)
    tetris.setOperation('w', myonCw, myonCcw)
    tetris.setOperation(' ', myonDrop, myonUp)
    tetris.setOperation('0', myonNewBlock, myonFinished)
    tetris.setOperation('1', myonNewBlock, myonFinished)
    tetris.setOperation('2', myonNewBlock, myonFinished)
    tetris.setOperation('3', myonNewBlock, myonFinished)
    tetris.setOperation('4', myonNewBlock, myonFinished)    
    tetris.setOperation('5', myonNewBlock, myonFinished)   
    tetris.setOperation('6', myonNewBlock, myonFinished)   

    idxType = str(randint(0, a.nBlockTypes))
    a.state = a.accept(idxType)

    while a.select_mode() :
        continue

    while True :
        key = input('Enter a key from [ q (quit), a (left), d (right), s (down), w (rotate), \' \' (drop) ] : ')
        a.state = a.accept(key)
        if a.state == TetrisState.Finished:
            break
        
        os.system("clear")
        a.print_oScreen()
        
        if a.state == TetrisState.NewBlock :
            idxType = str(randint(0, a.nBlockTypes))
            a.state = a.accept(idxType)
            if a.state == TetrisState.Finished : break 
            os.system("clear")
            a.print_oScreen()



if __name__ == "__main__":
    main()
else:
    print("Do not run the main module elsewhere.")
