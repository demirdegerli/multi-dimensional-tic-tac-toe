starter = "X" # "X" or "O"
interactive_mode = False
bot_sleep = True

from random import randint
from time import sleep
import re


canvas = []

for i in range(9):
    tmp_arr = []
    for j in range(9):
        tmp_arr.append(" ")
    canvas.append(tmp_arr)

def render_canvas():
    print("**************************")

    print(f"""| {canvas[0][0]} {canvas[0][1]} {canvas[0][2]} | {canvas[1][0]} {canvas[1][1]} {canvas[1][2]} | {canvas[2][0]} {canvas[2][1]} {canvas[2][2]} |
| {canvas[0][3]} {canvas[0][4]} {canvas[0][5]} | {canvas[1][3]} {canvas[1][4]} {canvas[1][5]} | {canvas[2][3]} {canvas[2][4]} {canvas[2][5]} |
| {canvas[0][6]} {canvas[0][7]} {canvas[0][8]} | {canvas[1][6]} {canvas[1][7]} {canvas[1][8]} | {canvas[2][6]} {canvas[2][7]} {canvas[2][8]} |
-------------------------
| {canvas[3][0]} {canvas[3][1]} {canvas[3][2]} | {canvas[4][0]} {canvas[4][1]} {canvas[4][2]} | {canvas[5][0]} {canvas[5][1]} {canvas[5][2]} |
| {canvas[3][3]} {canvas[3][4]} {canvas[3][5]} | {canvas[4][3]} {canvas[4][4]} {canvas[4][5]} | {canvas[5][3]} {canvas[5][4]} {canvas[5][5]} |
| {canvas[3][6]} {canvas[3][7]} {canvas[3][8]} | {canvas[4][6]} {canvas[4][7]} {canvas[4][8]} | {canvas[5][6]} {canvas[5][7]} {canvas[5][8]} |
-------------------------
| {canvas[6][0]} {canvas[6][1]} {canvas[6][2]} | {canvas[7][0]} {canvas[7][1]} {canvas[7][2]} | {canvas[8][0]} {canvas[8][1]} {canvas[8][2]} |
| {canvas[6][3]} {canvas[6][4]} {canvas[6][5]} | {canvas[7][3]} {canvas[7][4]} {canvas[7][5]} | {canvas[8][3]} {canvas[8][4]} {canvas[8][5]} |
| {canvas[6][6]} {canvas[6][7]} {canvas[6][8]} | {canvas[7][6]} {canvas[7][7]} {canvas[7][8]} | {canvas[8][6]} {canvas[8][7]} {canvas[8][8]} |""")

    print("**************************")


def is_empty(arr):
    for i in arr:
        if i != 0:
            return False
    return True

### MAIN ALGORITHM ###

def check_winner(arr, player):
    # Checks if the player can win in the next move and returns the position
    # check rows
    for i in range(0, 9, 3):
        if arr[i] == arr[i + 1] == player and arr[i + 2] == " ":
            return i + 2
        if arr[i] == arr[i + 2] == player and arr[i + 1] == " ":
            return i + 1
        if arr[i + 1] == arr[i + 2] == player and arr[i] == " ":
            return i

    # check columns
    for i in range(3):
        if arr[i] == arr[i + 3] == player and arr[i + 6] == " ":
            return i + 6
        if arr[i] == arr[i + 6] == player and arr[i + 3] == " ":
            return i + 3
        if arr[i + 3] == arr[i + 6] == player and arr[i] == " ":
            return i

    # check diagonals
    if arr[0] == arr[4] == player and arr[8] == " ":
        return 8
    if arr[0] == arr[8] == player and arr[4] == " ":
        return 4
    if arr[4] == arr[8] == player and arr[0] == " ":
        return 0

    if arr[2] == arr[4] == player and arr[6] == " ":
        return 6
    if arr[2] == arr[6] == player and arr[4] == " ":
        return 4
    if arr[4] == arr[6] == player and arr[2] == " ":
        return 2

    return None

def best_move(arr, player):
    # check if the board is empty, play the center (index 4)
    if is_empty(arr):
        return 4  # center

    # check if the current player can win
    win_move = check_winner(arr, player)
    if win_move is not None:
        return win_move

    # check if the opponent can win in the next move and block them
    opponent = 'X' if player == 'O' else 'O'
    block_move = check_winner(arr, opponent)
    if block_move is not None:
        return block_move

    # if center is available then take it
    if arr[4] == " ":
        return 4

    # choose a corner if available (possible: 0,2,6,8)
    corners = [0, 2, 6, 8]
    for corner in corners:
        if arr[corner] == " ":
            return corner

    # otherwise, pick any remaining empty cell
    for i in range(9):
        if arr[i] == " ":
            return i
        
### MAIN ALGORITHM ###

def check_win_status(arr):
    # check rows
    for i in range(0, 9, 3):
        if arr[i] == arr[i + 1] == arr[i + 2] and arr[i] != " ":
            return (arr[i], [i, i+1, i+2])

    # check columns
    for i in range(3):
        if arr[i] == arr[i + 3] == arr[i + 6] and arr[i] != " ":
            return (arr[i], [i,i+3,i+6])

    # check diagonals
    if arr[0] == arr[4] == arr[8] and arr[0] != " ":
        return (arr[0], [0,4,8])
    if arr[2] == arr[4] == arr[6] and arr[2] != " ":
        return (arr[2], [2,4,6])

    return (None, None)

def check_inner_wins(pos):
    winner, win_move = check_win_status(canvas[pos])
    if winner is not None:
        print(f"Winner in the {pos}. cell is", winner)
        for index in win_move:
            if winner == "X":
                canvas[pos][index] = "x"
            else:
                canvas[pos][index] = "o"

def check_outer_wins():
    overview = []
    for i in canvas:
        if "x" in i:
            overview.append("X")
        elif "o" in i:
            overview.append("O")
        else:
            overview.append(" ")
    return check_win_status(overview)[0]

def show_overview():
    overview = []
    for i in canvas:
        if "x" in i:
            overview.append("X")
        elif "o" in i:
            overview.append("O")
        else:
            overview.append(" ")
    print(f"""Overview:
{overview[0]} | {overview[1]} | {overview[2]}
---------
{overview[3]} | {overview[4]} | {overview[5]}
---------
{overview[6]} | {overview[7]} | {overview[8]}""")

current_player = starter

outer = randint(0,8)
inner = randint(0,8)
canvas[outer][inner] = current_player
last_move = [outer, inner]
print(f"Start move from {current_player} ({outer},{inner})")
render_canvas()
if bot_sleep:
    sleep(2)

moves = 1

break_main_loop = False
while True:
    outer_win = check_outer_wins()
    if outer_win is not None:
        print(outer_win, "won the game!")
        show_overview()
        break

    # current player selects a random cell if the game in the current cell is ended
    tries = []
    while last_move[1] != None and "x" in canvas[last_move[1]] or "o" in canvas[last_move[1]] or " " not in canvas[last_move[1]]:
        if len(tries) == 9:
            print("Draw!")
            show_overview()
            break_main_loop = True
            break
        random = randint(0,8)
        if not interactive_mode or current_player == starter:
            last_move[1] = random
        else:
            last_move[1] = None
        if random not in tries:
            tries.append(random)

    if break_main_loop:
        break

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

    if not interactive_mode or current_player == starter:
        best_move_pos = best_move(canvas[last_move[1]], current_player)
        if best_move_pos == None:
            break
        canvas[last_move[1]][best_move_pos] = current_player
        print(current_player, "is placing to", f"{last_move[1]},{best_move_pos}")
    else:
        def check_input(user_input):
            pattern = r'^[0-8],[0-8]$'
            return re.match(pattern, user_input)
        human = ""
        def ask_input():
            global human
            human = input(f"Write your move as {current_player} (outer,inner): ")
            while not check_input(human):
                print("Invalid move!")
                ask_input()
            if canvas[int(human[0])][int(human[2])] != " ":
                print("That cell is not empty!")
                ask_input()
            if "x" in canvas[int(human[0])] or "o" in canvas[int(human[0])] or " " not in canvas[int(human[0])]:
                print("The alt-game has ended in the block that contains the cell you selected.")
                ask_input()
            if int(human[0]) != last_move[1] and last_move[1] != None:
                print("Invalid move!")
                ask_input()
        ask_input()
        canvas[int(human[0])][int(human[2])] = current_player
        print(current_player, "(human)", "has placed to", f"{int(human[0])},{int(human[2])}")
        last_move[1] = int(human[0])
    
    check_inner_wins(last_move[1])
    if not interactive_mode or current_player == starter:
        last_move = [last_move[1], best_move_pos]
    else:
        last_move = [int(human[0]), int(human[2])]
    moves += 1
    render_canvas()

    if interactive_mode:
        sleep(1)
    else:
        if bot_sleep:
            sleep(2)
