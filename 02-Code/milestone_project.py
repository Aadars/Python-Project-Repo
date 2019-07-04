board=['-','-','-','-','-','-','-','-','-','-']

#display board########################

#---------------------------- GAME STILL GONE---------------------------------------#

game_still_going = True



#---------------------------------------WHO WON? OR TIE ?-------------------------------------------#
winner = None

#----------------------------------------- WHOSE TURN ARE IS IT---------------------------------#

current_player='X'

#--------------------------------------------------------display board -------------------------------------------------#

def display_board():
    print(' | | ')
    print(  board[0]+'|'+board[1]+'|'+board[2])
    print(' | |')
    print('------')
    print(' | | ')
    print(  board[3]+'|'+board[4]+'|'+board[5])
    print(' | | ')
    print('------')
    print(  board[6]+'|'+board[7]+'|'+board[8])
    print(' | | ')

#----------------------------------- FOR PLAYING GAME ----------------------------------------------------------#

def play_game():
    global game_still_going
    display_board()

#------------------------------------------------ HANDEL TURN -----------------------------------------------------------------#
##--------------------- WHILE THE GAME IS STILL GOING----------#
    while game_still_going:
        # handel a single turn arbitrary player
        handel_turn(current_player)
        # check game is win by someone or Tie
        check_if_game_over()
        # Flip to the other player
        flip_player()
        
        
    if winner=='X' or winner=='O':
        print(winner+' , won the game')
        
    elif winner == None:
        print('Tie')
    
#-------------------------- HANDEL TURN --------------------------------#
    
def handel_turn(player):
    print(player + "'s Turn. ")
    position=input('choose your position from 1-9 : ')
    valid = False
    while not valid:
    
        while position not in ['1','2','3','4','5','6','7','8','9']:
            position=input('choose your position from 1-9 : ')
        position=int(position)-1

        if board[position] == '-':
            valid = True
        else:
            print('you cant go there again. ')
    
    board[position]=player
    
    display_board()


#----------------------------------- CHECK GAME IS OVER OR NOT---------------------------------------#
def check_if_game_over():
    
    check_for_winner()

    check_if_tie()    
    
        # win
        #check rows
        #check columns
        #check diagonals
    return
def check_for_winner():
    global winner
    row_winner = check_rows()
        
    column_winner = check_columns()
        #check diognals
    diagonal_winner = check_diognals()
    #tie
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

        
    return   

def check_rows():

#---------------------------------------- GLOBAL VARIABLE ASSIGN --------------------------------------#
    
    global game_still_going

#-------------------------------- ALL ARE SAME OR NOT --------------------------------------#
    
    row_1= board[0] == board[1] == board[2] != '-'
    row_2= board[3] == board[4] == board[5] != '-'
    row_3= board[6] == board[7] == board[8] != '-'

#------------------------------------------     RETURN THE WINNER X OR O ------------------------------------#
    
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
        
    return


def check_columns():

#---------------------------------------- GLOBAL VARIABLE ASSIGN --------------------------------------#
    
    global game_still_going

#-------------------------------- ALL ARE SAME OR NOT --------------------------------------#
    
    column_1 = board[0] == board[3] == board[6] != '-'
    column_2 = board[1] == board[4] == board[7] != '-'
    column_3 = board[2] == board[5] == board[8] != '-'

#------------------------------------------     RETURN THE WINNER X OR O ------------------------------------#
    
    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diognals():
    

#---------------------------------------- GLOBAL VARIABLE ASSIGN --------------------------------------#
    
    global game_still_going
    
    diagonal_1 = board[0] == board[4] == board[8] != '-'
    diagonal_2 = board[6] == board[4] == board[2] != '-'

    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return
#--------------------------------CHECK FOR TIE------------------------------#
def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return 
 

#---------------------------------- FLIP PLAYER -------------------------------------------------------#    
def flip_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X' 
    return

   
play_game()






    

    

