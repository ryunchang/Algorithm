from matrix import *
from tetris import *
from Ctetris import *


def main() :
    a = Ctetris() 

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
    
    tetris.setOperation('q', TetrisState.Running, myonFinished, TetrisState.Finished, myonFinished, TetrisState.Finished)
    tetris.setOperation('a', TetrisState.Running, myonLeft, TetrisState.Running, myonRight, TetrisState.Running)
    tetris.setOperation('d', TetrisState.Running, myonRight, TetrisState.Running, myonLeft, TetrisState.Running)
    tetris.setOperation('s', TetrisState.Running, myonDown, TetrisState.Running, myonUp, TetrisState.NewBlock)
    tetris.setOperation('w', TetrisState.Running, myonCw, TetrisState.Running, myonCcw, TetrisState.Running)
    tetris.setOperation(' ', TetrisState.Running, myonDrop, TetrisState.Running, myonUp, TetrisState.NewBlock)
    tetris.setOperation('0', TetrisState.NewBlock, myonNewBlock, TetrisState.Running, myonFinished, TetrisState.Finished)
    tetris.setOperation('1', TetrisState.NewBlock, myonNewBlock, TetrisState.Running, myonFinished, TetrisState.Finished)
    tetris.setOperation('2', TetrisState.NewBlock, myonNewBlock, TetrisState.Running, myonFinished, TetrisState.Finished)
    tetris.setOperation('3', TetrisState.NewBlock, myonNewBlock, TetrisState.Running, myonFinished, TetrisState.Finished)
    tetris.setOperation('4', TetrisState.NewBlock, myonNewBlock, TetrisState.Running, myonFinished, TetrisState.Finished)    
    tetris.setOperation('5', TetrisState.NewBlock, myonNewBlock, TetrisState.Running, myonFinished, TetrisState.Finished)   
    tetris.setOperation('6', TetrisState.NewBlock, myonNewBlock, TetrisState.Running, myonFinished, TetrisState.Finished)   

    idxType = str(randint(0, a.nBlockTypes))
    a.state = a.accept(idxType)

    while a.select_mode() :
        continue

    while True :
        key = input('Enter a key from [ q (quit), a (left), d (right), s (down), w (rotate), \' \' (drop) ] : ')
        a.state = a.accept(key)
        if a.state == TetrisState.Finished:
            break
        a.print_oScreen()

        if a.state == TetrisState.NewBlock :
            idxType = str(randint(0, a.nBlockTypes))
            a.state = a.accept(idxType)
            if a.state == TetrisState.Finished : break 
            a.print_oScreen()



if __name__ == "__main__":
    main()
else:
    print("Do not run the main module elsewhere.")
