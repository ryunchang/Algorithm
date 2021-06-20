
import random

board = ((1,2,3,4),(5,6,7,8),(8,7,6,5),(4,3,2,1))
board_faired = [[False, False, False, False],
                [False, False, False, False],
                [False, False, False, False],
                [False, False, False, False]]

player1_score = 0
player2_score = 0
turn_counter = 20

def main():
    global board, board_faired, player1_score, player2_score, turn_counter

    game_mode = int(input("Choose game mode (Static : 1, Random: 2) : "))
    if(game_mode == 2):
        board = init_random_board()
    
    whos_turn = 1
    while(turn_counter):
        print("------------------------")
        show_board(board, board_faired)
        print(whos_turn, "player turn!  ", turn_counter, "turns remain..")
        location = input_location()

        if (check_card(board, board_faired, location)):
            continue

        if(match_card(board, board_faired, location)):
            revision_score(board, location, whos_turn)
        else:
            print("Not matched..")

        if(whos_turn == 1): whos_turn = 2
        else: whos_turn = 1
        
        if( all(board_faired[0]) and all(board_faired[1]) and
                all(board_faired[2]) and all(board_faired[3]) ):
            print("Find all card!")
            break
        turn_counter -= 1

    if(player1_score > player2_score): print("player1 win!!")
    elif(player1_score < player2_score): print("player2 win!!")
    else: print("Draw")


def init_random_board():
    random_board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(0, 3+1, 1):
        for j in range(0, 3+1, 1):
            while(True):
                num = random.randrange(1, 8+1)
                if (random_board[0].count(num) + random_board[1].count(num) + 
                        random_board[2].count(num) + random_board[3].count(num)) < 2 :
                    random_board[i][j] = num
                    break
    return random_board

def show_board(board, board_faired):
    print("   |  1  2  3  4 ")
    print(" ---------------")
    for i in range(0, 4, 1):
        print(i+1, " | ", end="")
        for j in range(0, 4, 1):
            if(board_faired[i][j]): print("", board[i][j], end=" ")
            else: print(" x ", end="")
        print()

def input_location():
    first, second = input("Put number : ").split()
    row1, column1 = int(first) // 10, int(first) % 10
    row2, column2 = int(second) // 10, int(second) % 10
    return row1-1, column1-1, row2-1, column2-1

def match_card(board, board_faired, location):
    row1, column1, row2, column2 = location
    if(board[row1][column1] == board[row2][column2]):
        board_faired[row1][column1] = True
        board_faired[row2][column2] = True
        return True
    else:
        return False

def check_card(board, board_faired, location):
    row1, column1, row2, column2 = location
    if (row1 < 0 or row1 > 3) or (column1 < 0 or column1 > 3):
        print("Error! first card location is not correct")
        return True
    elif (row2 < 0 or row2 > 3) or (column2 < 0 or column2 > 3):
        print("Error! second card location is not correct")
        return True
    elif row1 == row2 and column1 == column2 :
        print("Error! Choose different card")
        return True
    elif board_faired[row1][column1] == True or board_faired[row2][column2] == True :
        print("Error! Already Choosen")
        return True
    else:
        board_faired[row1][column1] = True; board_faired[row2][column2] = True
        show_board(board, board_faired)
        board_faired[row1][column1] = False; board_faired[row2][column2] = False
        return False
        
def revision_score(board, location, whos_turn):
    global player1_score, player2_score
    if(board[location[0]][location[1]] == 7):
        print("Lucky")
        if whos_turn == 1 : player1_score += 2
        else : player2_score += 2
    else:
        if whos_turn == 1 : player1_score += 1
        else : player2_score += 1
    print(whos_turn, "player matching card!!  NOW, 1 player : ", player1_score, ",  2 player : ", player2_score)

if __name__ == "__main__":
    main()




