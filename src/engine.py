import stone_class as sc
import player_class as pc
import board


def print_bd():
    for i in board:
        for f in i:
            if f in sc._all_st:
                print(' O ', end = " ")
            else:
                print(f, end = " ")
        print("\n")

# Initialize players :
white = player('w')
black = player('b')

move_idx = 0

while True:
    if move_idx % 2 == 0:
        # move white
        move_idx += 1 
    else:
        # move black
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
