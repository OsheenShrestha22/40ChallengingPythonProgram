def draw_board(char_num):
    print("\n\t\tTic Tac Toe")
    print("\t~~~~~~~~~~~~~~~~~~~~~~")
    print(f"\t||  {char_num[0]}  ||  {char_num[1]}  ||  {char_num[2]}  ||")
    print(f"\t||  {char_num[3]}  ||  {char_num[4]}  ||  {char_num[5]}  ||")
    print(f"\t||  {char_num[6]}  ||  {char_num[7]}  ||  {char_num[8]}  ||")


def get_player_input(player_char,char_list):
    """Get a player move until it is a valid move on the board with no piece currently there."""
    while True:
        #Get User Input
        player_move = int(input(player_char+": Where would you like to place your piece(1-9):"))
        #Move is on board
        if player_move >0 and player_move <10:
            #Move is an empty spot
            if char_list[player_move -1] == '_':
                return player_move
            else:
                print("That spot has been already choosen.Try again")
        else:
            print("That is not a spot on the board.Try again")


def place_charc_on_board(player_char,player_move,char_list):
    """Put the player characters at the correct spot on th board"""
    char_list[player_move-1] =player_char

def is_winner(pC,cL):
    """Return a Bool if the give player is winner"""
    return ((cL[0] == pC and cL[1] == pC and cL[2] == pC) or  #Victory in the first row
            (cL[3] == pC and cL[4] == pC and cL[5] == pC) or  # Victory in the second row
            (cL[6] == pC and cL[7] == pC and cL[8] == pC) or  # Victory in the third row
            (cL[0] == pC and cL[3] == pC and cL[6] == pC) or  # Victory in the first column
            (cL[1] == pC and cL[4] == pC and cL[7] == pC) or  # Victory in the second column
            (cL[2] == pC and cL[5] == pC and cL[8] == pC) or  # Victory in the third coulmn
            (cL[0] == pC and cL[4] == pC and cL[8] == pC) or  # Victory in the first diagonal
            (cL[2] == pC and cL[4] == pC and cL[6] == pC)     # Victory in the second diagonal
            )


#Main Code
#Defining a variables
player_1= 'X'
player_2= '0'
c_list=['_']*9
n_list =['1','2','3','4','5','6','7','8','9']

#Draw the initial state of the draw board
draw_board(n_list)
draw_board(c_list)

while True:
    #Player 1 turn
    #Get the Player Move
    move = get_player_input(player_1,c_list)
    #Put move on the board
    place_charc_on_board(player_1,move,c_list)
    #Redraw th game board
    draw_board(n_list)
    draw_board(c_list)
    #Check to see if the player 1 win the game
    if is_winner(player_1,c_list):
        print("Player 1 wins")
        break
    elif "_" not in c_list:
        print("The game is a tie")
        break
    #Player 2 turn
    #Get the Player Move
    move = get_player_input(player_2,c_list)
    #Put move on the board
    place_charc_on_board(player_2,move,c_list)
    #Redraw th game board
    draw_board(n_list)
    draw_board(c_list)
    #Check to see if the player 1 win the game
    if is_winner(player_2,c_list):
        print("Player 2 wins")
        break


