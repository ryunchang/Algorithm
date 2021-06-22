from matrix import *
from tetris import *



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
    
    idxType = str(randint(0, a.nBlockTypes))
    a.state = a.accept('0' + idxType)

    while a.select_mode() :
        continue

    while True :
        key = input('Enter a key from [ q (quit), a (left), d (right), s (down), w (rotate), \' \' (drop) ] : ')
        a.state = a.accept(key + idxType)
        if a.state == TetrisState.Finished:
            break
        a.print_oScreen()

        if a.state == TetrisState.NewBlock :
            idxType = str(randint(0, a.nBlockTypes))
            a.state = a.accept('0' + idxType)
            if a.state == TetrisState.Finished :
                print('Game Over!!!')
                break 
            a.print_oScreen()

if __name__ == "__main__":
    main()
else:
    print("Do not run the main module elsewhere.")
