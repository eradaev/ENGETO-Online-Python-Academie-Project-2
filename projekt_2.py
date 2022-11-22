"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Evgeniy Radaev
email: eradaev@gmail.com
discord: Eugene_2022#3697
"""
# pozdrav uzivatele
print("Welcome to Tic Tac Toe")
print("=" * 45)

# pravidla hry
print("""GAME RULES:
Each player can place one mark (or stone) 
per turn on the 3 x 3 grid by entering the 
corresponding number:
-------------
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
-------------
The WINNER is the one who succeeds in placing
three of their marks in a:
        * horizontal,
        * vertical,
        * or diagonal row. """)
print("=" * 45)
print("Let's start the game")
print("-" * 45)

grid = [1, 2, 3, 4, 5, 6, 7, 8, 9]
grid_empty = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


# hraci plocha
def draw_grid(grid_empty):
    print("-" * 13)
    for i in range(3):
        print("|", grid_empty[0 + i * 3], "|", grid_empty[1 + i * 3], "|", grid_empty[2 + i * 3], "|")
        print("-" * 13)


# volba pozice
def place_mark(player_mark):
    valid = False
    while not valid:
        move_number = input("Player " + player_mark + " | Please enter your move number: ")
        try:
            move_number = int(move_number)
        except:
            print("Incorrect entry. Please enter the number!")
            continue
        if move_number >= 1 and move_number <= 9:
            if (str(grid[move_number - 1]) not in "XO"):
                grid[move_number - 1] = player_mark
                grid_empty[move_number - 1] = player_mark
                valid = True
            else:
                print("This cell has already been taken!")
        else:
            print("Incorrect entry. Please enter the number from 1 to 9.")


# vyhodnocovani viteznych kombinaci
def check_win_comb(grid):
    win_combs = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_combs:
        if grid[each[0]] == grid[each[1]] == grid[each[2]]:
            return grid[each[0]]
    return False


def main(grid):
    counter = 0
    win = False
    while not win:
        draw_grid(grid_empty)
        if counter % 2 == 0:
            place_mark("X")
        else:
            place_mark("O")
        counter += 1
        if counter > 4:
            result = check_win_comb(grid)
            if result:
                print("Congratulations, the player", result, "WON!")
                win = True
                break
        if counter == 9:
            print("IT'S A DRAW!")
            break
    draw_grid(grid_empty)


main(grid)
