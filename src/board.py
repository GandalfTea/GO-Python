
BRD_SIZE = 19

# Define the board matrix
board = []
for i in range(BRD_SIZE + 1):
    if i < BRD_SIZE:
        board.append([])
        board[i].append(i + 1)

for i in range(len(board)):
    for j in range(BRD_SIZE):
        board[i].append(None)
a = []
for i in range(BRD_SIZE + 1):
    a.append(i)
board.append(a)

for i in range(len(board)):
    board[i].append(i + 1)


