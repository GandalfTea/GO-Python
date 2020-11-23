
boardsize = 5
gs = []

for i in range(0, boardsize):
    gs.append([])
    for j in range(0, boardsize):
        gs[i].append('-')

    
def printboard(gs):
    global boardsize
    for row in gs:
        rowprint = ''
        for element in row:
            rowprint += element
            rowprint += ' '
        print(rowprint)

printboard(gs)

def readable(gs):
    readthis = ''
    readthis += '<<'
    for row in gs:
        for element in row:
            readthis += element
    readthis += '>>'
    return readthis

print(readable(gs))

def iter(direction, group, loss, hit):
    j = 0
    i = 0
    global boardsize
    global parmimeter
    while i < boardsize:
        j = 0
        hit = 0
        while j < boardsize:
            if(direction == 'down') or (direction == 'above'):
                if [j,i] in group:
                    hit = 1
                elif (hit == 1) & ([j,i] not in group):
                    loss = 1
                if (hit == 1) & (loss == 1):
                    parmimeter.append([j,i])
                    hit = 0
                    loss = 0
            elif(direction == 'left') or (direction == 'right'):
                if [i,j] in group:
                    hit = 1
                elif (hit == 1) & ([i,j] not in group):
                    loss = 1
                if (hit == 1) & (loss == 1):
                    parmimeter.append([i,j])
                    hit = 0
                    loss = 0
            if(direction == 'left') or (direction == 'above'):
                j -= 1
            elif(direction == 'right') or (direction == 'down'):
                j += 1
        if(direction == 'left') or (direction == 'above'):
            i -= 1
        elif(direction == 'right') or (direction == 'down'):
            i += 1

def groupParmimeter(group):
    parmimeter = []
    global boardsize
    hit = 0
    loss = 0

    iter('down', group, loss, hit)
    iter('right', group, loss, hit)
    iter('above', group, loss, hit)
    iter('left', group, loss, hit)
    
    return parmimeter

#groupParmimeter(gs)







