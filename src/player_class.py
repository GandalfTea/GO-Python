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
        print(cord)
        for st in self.container:
            if st not in stc._pl_st:
                st.pl(cord[0], cord[1])
                return

    def capture(self ,size):
        self.captured += size
        return


