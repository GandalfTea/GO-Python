import stone_class as stc

class player:

    def __init__(self, color):

        if color == 'b':
            self.STNUM = 181
        elif color == 'w':
            self.STNUM = 180
        else:
            raise Exception("Unxpected color value.")

        self.c = color
        self.captured = 0
        self.container = []

        for i in range(self.STNUM):
            self.container.append(stc.st())

        for st in self.container:
            st.c = color


    def play(self, cord):
        for st in self.container:
            if st not in stc._pl_st:
                st.pl(cord[0], cord[1])
                return st


    def capture(self, st):

        groups = []

        # Check self and nb for capture
        # this may each return a captured group or just a captured stone.
        # add all retulting captures to and return groups[]

        groups.append(st.capture())
        
        # Different nb might return different captured groups.
        for nb in st.lnb:
            if nb != 0:
                groups.append(nb.capture())
        if groups is not None:
                return groups


