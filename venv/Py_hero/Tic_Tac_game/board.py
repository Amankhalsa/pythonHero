import  random
print("Tic-Tac-Toe game...!")
game_input=["Null","x","0","x","0","x","0","x","0","x"]

# board
def board(game_input):
    print(game_input[7]+"|"+game_input[8]+"|"+game_input[9])
    print(game_input[4]+"|"+game_input[5]+"|"+game_input[6])
    print(game_input[1]+"|"+game_input[2]+"|"+game_input[3])
# board(game_input)
# marker
def player_input():
    marker =" "
    while marker !="x" and marker !="0":

        marker =input("Player 1: Please choose your marker:")
    if marker =="x":
        return ("x","0")
    else:
        return ("0","x")
# player_input()
# player2,player1 = player_input()
# print(f"{player1}")
# print(f"{player2}")
def put_marker(game_input,marker,position):
    game_input[position]=marker
    # game_input[2]="marker2"
    # board(game_input)
def win(game_input, marker):
    return ((game_input[7]==game_input[8]==game_input[9]==marker) or
            (game_input[4]==game_input[5]==game_input[6]==marker) or
            (game_input[1]==game_input[2]==game_input[3]==marker) or
            (game_input[1]==game_input[5]==game_input[9]==marker) or
            (game_input[7]==game_input[5]==game_input[3]==marker) or
            (game_input[1]==game_input[4]==game_input[7]==marker) or
            (game_input[2]==game_input[5]==game_input[8]==marker) or
            (game_input[3]==game_input[6]==game_input[9]==marker ))
# print(win(game_input,"x"))
# Choose player using random function
def choose_player():
    player=random.randint(1,2)
    # print(plaayer)
    if player==1:
        return "Player 1 (Aman):"
    else:
        return "Player 2 (computer):"
# choose_player()
# check for empty space
def space(game_input,position):
   return  game_input[position] ==" "

def full_board_check(game_input):
    for i in range(1,10):
        if space(game_input,i):
            return False

    return True
#player choise of marker placement
def Player_choise(game_input):
    position =0
    while position not in [1,2,3,4,5,6,7,8,9] or not space(game_input, position):
        position = int(input("Please choose your position (1-9) on Numpad:"))
    return  position

#whould you lie to play again
def play_again():
    choice= input("\tWould you like to play again [y/n]:")
    return  choice=="y"

# Game playing macanism
while True:
    the_board=[" "]*10
    player_1,player_2=player_input()
    print(player_1+ " is Player_1 sign")
    print(player_2+ " is Player_2 sign")
    turn =choose_player()
    print(turn+" have won toss")
    print(turn+ " will Play first")

    play_game= input("Are you ready to play[y/n]:")
    if play_game=="y":
        game_on=True
    else:
        game_on=False
    while game_on:
        if turn=="player_1":
            board(the_board)
            position=Player_choise(the_board)
            put_marker(the_board,player_1,position)
            if win(the_board,player_1):
                board(the_board)
                print("\t\tGame is over")
                print("Hurrah....! \n\tplayer 1 (Aman) have won this game\n")
                game_on=False
            else:
                if full_board_check(the_board):
                    board(the_board)
                    print("Game tie")
                    game_on=False
                    print("\t\tGame is over")

                else:
                    turn="player_2"
                    print("\t\tGame is on")

#---------------------------------------------------------------------
        else:
            board(the_board)
            position = Player_choise(the_board)
            put_marker(the_board, player_2, position)
            if win(the_board, player_2):
                board(the_board)
                print("\t\tGame is over")
                print("Hurrah....! \n\tplayer 2 (Computer) have won this game\n")
                game_on = False
            else:
                if full_board_check(the_board):
                    board(the_board)
                    print("Game tie")
                    game_on = False
                    print("\t\tGame is over")
                else:
                    turn = "player_1"
                    print("\t\tGame is on")

    if not  play_again():
        break
