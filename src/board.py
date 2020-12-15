

BRD_SIZE = 19

# Define the board matrix
board = []
for i in range(BRD_SIZE - 1):
    board.append([])

for i in range(len(board)):
    for j in range(BRD_SIZE - 1):
        board[i].append(None)
