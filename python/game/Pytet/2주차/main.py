from matrix import *
from tetris import *


def main() :
    a = tetris() 
    key = 'null'

    idxType = str(randint(0, a.nBlockTypes))
    a.state = a.accept('0' + idxType)

    while a.select_mode() :
        continue

    while True :
        key = input('Enter a key from [ q (quit), a (left), d (right), s (down), w (rotate), \' \' (drop) ] : ')
        if key == 'q':
            break
        a.state = a.accept(key + idxType)
        a.print_oScreen()

        if a.state == TetrisState.NewBlock :
            a.delete_fullLine()
            idxType = str(randint(0, a.nBlockTypes))
            a.state = a.accept('0' + idxType)
            a.make_newBlock()
            if a.state == TetrisState.Finished :
                print('Game Over!!!')
                break 
            a.print_oScreen()


if __name__ == "__main__":
    main()
else:
    print("Do not run the main module elsewhere.")
