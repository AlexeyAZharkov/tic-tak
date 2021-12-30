player_name = input("Hello new player! What's your name? \n")
print('In order to make a move, you need to enter the cell number:\n')
print('1|2|3\n4|5|6\n7|8|9\n')

# a list containing the sums of columns, rows, and diagonals
game_calculation = [0,0,0,0,0,0,0,0]
# Priority of the cell sum in the game
prior = [2,-2,1,-1,0]

def write_game(play):
    # Displaying the game field
    fild = ''
    number = 0
    for i in play:
        number += 1
        if i == 1:
            fild +='x'
        elif i == -1:
            fild +='o'
        else:
            fild +='_'
        if number == 3 or number == 6 or number == 9:
            fild +='\n'
        else:
            fild +='|'
    print(fild)


def game_calculate(play):
    # Calculate the sum of all columns, rows and diagonals.
    # The function returns a list
    game_calculation[0] = play[0] + play[1] + play[2]
    game_calculation[1] = play[3] + play[4] + play[5]
    game_calculation[2] = play[6] + play[7] + play[8]
    game_calculation[3] = play[0] + play[3] + play[6]
    game_calculation[4] = play[1] + play[4] + play[7]
    game_calculation[5] = play[2] + play[5] + play[8]
    game_calculation[6] = play[0] + play[4] + play[8]
    game_calculation[7] = play[6] + play[4] + play[2]
    return game_calculation


def is_win(calculation):
    # Determining the winner using a list calculated by the function 'game_calculate'
    for i in calculation:
        if i == 3:
            print(f'{player_name}! You WIN!!!')
            return True
        elif i == -3:
            print(f'{player_name}! You lose...')
            return True
    return False


def comp_move(play):
    # Calculating the computer's progress. Cells are calculated in turn,
    # according to their priority. The calculated number is compared with the number from the list
    for pr in prior:
        if play[4] == 0 and (play[0] + play[8] == pr or play[2] + play[6] == pr
        or play[1] + play[7] == pr or play[3] + play[5] == pr):
            return 4
        if play[0] == 0 and (play[1] + play[2] == pr or play[3] + play[6] == pr
        or play[4] + play[8] == pr):
            return 0
        if play[2] == 0 and (play[0] + play[1] == pr or play[5] + play[8] == pr
        or play[4] + play[6] == pr):
            return 2
        if play[6] == 0 and (play[0] + play[3] == pr or play[7] + play[8] == pr
                             or play[4] + play[2] == pr):
            return 6
        if play[8] == 0 and (play[2] + play[5] == pr or play[6] + play[7] == pr
                             or play[4] + play[0] == pr):
            return 8
        if play[1] == 0 and (play[0] + play[2] == pr or play[4] + play[7] == pr):
            return 1
        if play[3] == 0 and (play[0] + play[6] == pr or play[4] + play[5] == pr):
            return 3
        if play[5] == 0 and (play[8] + play[2] == pr or play[4] + play[3] == pr):
            return 5
        if play[7] == 0 and (play[1] + play[4] == pr or play[6] + play[8] == pr):
            return 7

play_list = [0,0,0,0,0,0,0,0,0]

number_of_moves = 0
game_over = False
while not game_over:
    user_move = int(input(f'{player_name}! Enter the cell number: '))
    while play_list[user_move-1] != 0:
        user_move = int(input('Occupied cell! Enter another cell number: '))
    number_of_moves += 1
    play_list[user_move-1] = 1
    write_game(play_list)
    game_over = is_win(game_calculate(play_list))
    if number_of_moves < 8:
        comp_move_cell = comp_move(play_list)
        play_list[comp_move_cell] = -1
        print("Ok, I'll try to answer like this:")
        write_game(play_list)
        number_of_moves += 1
        game_over = is_win(game_calculate(play_list))
    else:
        print("It is draw!")
        game_over = True


