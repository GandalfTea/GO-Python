import stone_class as sc
import player_class as pc
from board import board


def print_bd():
    for i in board:
        for f in i:
            if f in sc._all_st:
                print(' O ', end = " ") if f.c == "w" else print(' @ ', end = " ")
            elif isinstance(f, int):
                if f == 0:
                    print("     ", end = "")
                # Why TF is there a 20 here
                elif f == 20:
                    continue
                elif f >= 10:
                    print(f, end = "  ")
                else:
                    print(f, end = "   ")
            else:
                print(" . ", end = " ")
        print("\n")

def ask_move():
    a = int(input("X : "))
    b = int(input("Y : "))
    return (b - 1, a)


# Initialize players :
white = pc.player('w')
black = pc.player('b')
move_idx = 0


while True:
    if move_idx % 2 == 0:
        # move white
        white.play(ask_move())
        print_bd()
        move_idx += 1 
    else:
        # move black
        black.play(ask_move())
        print_bd()
        move_idx += 1 
        


# Ask for move
# Display board

# Count Teritory:
#   adapt the st iterator to empty slots and look
#   for neighbours.


# initialize players
# give players turn
# detect strings and groups
# count teritory
# end game
