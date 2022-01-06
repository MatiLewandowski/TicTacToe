from IPython.display import clear_output

#funkcja wyswietlania tablicy
def pr_board(board):
    clear_output()
    print(board[:3])
    print(board[3:6])
    print(board[6:])

#funkcja rozpoczecia gry - ustawienie graczy i wybor znaku
def game_start(dict1):
    print('Welcome to Tic Tac Toe!')
    sign=input("Player1: would you like to play 'X' or 'O'? ")
    sign1=sign.upper()
    if sign1=='O':
        dict1['player1']='O'
        dict1['player2']='X'
    return dict1

#czy mozemy rozpoaczac gre?

def can_we_start(dict1):
    decyzja=False
    while decyzja==False:
        decyzja_uzytkownika=input('Ok, player1 will go first using sign: {}. Can we start? (type Y or N)'.format(dict1['player1']))
        if decyzja_uzytkownika=='Y':
            decyzja=True

#check czy wygral
def check_for_win(board,dict1,win):
    lista=[0,3,6]
    lista1=[0,1,2]
    lista2=[0,4,8]
    lista3=[2,4,6]
    #horizontal win
    for item in lista:
        trojka=set(board[item:item+3])
        if len(trojka)==1:
            trojka=list(trojka)
            if trojka[0]==' ':
                win=0
                continue
            if trojka[0]==dict1['player1']:
                print('player1 wins!')
                win=1
                return win
            else:
                print('player2 wins!')
                win=2
                return win
    
    #vertical win
    for item in lista1:
        trojka=set(board[item::3])
        if len(trojka)==1:
            trojka=list(trojka)
            if trojka[0]==' ':
                win=0
                continue
            if trojka[0]==dict1['player1']:
                print('player1 wins!')
                win=1
                return win
            else:
                print('player2 wins!')
                win=2
                return win

    pomocnicza=[]
    #przekatna
    for item in lista2:
        pomocnicza+=board[item]
    trojka=set(pomocnicza)
    if len(trojka)==1:
        trojka=list(trojka)
        if trojka[0]==' ':
            win=0
        if trojka[0]==dict1['player1']:
            print('player1 wins!')
            win=1
            return win
        if trojka[0]==dict1['player2']:
            print('player2 wins!')
            win=2
            return win

    pomocnicza=[]

    for item in lista3:
        pomocnicza+=board[item]
    trojka=set(pomocnicza)
    if len(trojka)==1:
        trojka=list(trojka)
        if trojka[0]==' ':
            win=0
        if trojka[0]==dict1['player1']:
            print('player1 wins!')
            win=1
            return win
        if trojka[0]==dict1['player2']:
            print('player2 wins!')
            win=2
            return win

    return win   




#ruch uzytkownika i check czy wygral
def move(board,dict1,priority,win):
    acc_range=range(1,10)
    move_counter=0
    
    while move_counter<2 and win==0:
        ruch_player='wrong'
        within_range=False
        win=check_for_win(board,dict1,win)
        print(win)
        while ruch_player.isdigit()==False or within_range==False or board[int(ruch_player)-1]!=' ':
            if win==0:
                ruch_player=input('{} Choose a number from 1 to 9 to make a move: '.format(priority))

                if ruch_player.isdigit()==False:
                    print("Sorry! You didn't put a digit 1-9, try again!")

                if ruch_player.isdigit()==True:
                    if int(ruch_player) not in acc_range:
                        print('Sorry! Your number is not within 1-9. Try again!')
                    else:
                        within_range=True
                if board[int(ruch_player)-1]!=' ':
                    print('sorry, this place is already taken!')
            else:
                return win
        if win==0:        
            board[int(ruch_player)-1]=dict1[priority]
        pr_board(board)

        move_counter+=1
        priority='player2'
    return win           


def play_again():
    game_on=input('would you like to play again? (Y or N)')
    if game_on=='Y':
        return True
    if game_on=='N':
        return False



#main game
play_a=True
while play_a==True:
    #pusta tablica na poczatek
    board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
    dict_sign={'player1':'X', 'player2':'O'}
    player_prior='player1'
    winner=0
    win_check=0
    game_start(dict_sign)
    can_we_start(dict_sign)
    pr_board(board)
    while winner==0:
        winner=move(board,dict_sign,player_prior,winner)
    play_a=play_again()






