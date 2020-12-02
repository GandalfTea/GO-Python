

_all_st = []    #all stones
_pl_st = []     #played stones

class st:
    def __init__(self):
        self.x = 0
        self.y = 0
        self._all_nb = []

        _all_st.append(self)

    def __str__(self):
        if self in _pl_st:
            return "X : " + str(self.x) + ", Y : " + str(self.y)
        else:
            raise Exception("The stone has not been played yet.")

    def pl(self, x, y):
        self.x = x
        self.y = y
        _pl_st.append(self)
        self.lnb = self.nb()
        #print("string x :", x, "string y :", y)

    def nb(self):
        lnb = []
        for st in _all_st:
            #print("I will tel you a secreat.")
            if st.x == self.x and st.y == (self.y - 1):
                #print("I was the wierd duck")
                lnb.append(st)
            elif st.x == self.x and st.y == (self.y + 1):
                #print("I was the wierd duck")
                lnb.append(st)
            elif st.x == (self.x - 1) and st.y == self.y:
                #print("I was the wierd duck")
                lnb.append(st)
            elif st.x == (self.x + 1) and st.y == self.y:
                #print("I was the wierd duck")
                lnb.append(st)
            else:
                continue
            for i in lnb:
                print("Main : ", self)
                print(i)
        return lnb


    def _iter(self):
        # TODO: Test time with : time.time()
        temp_nb = []    # hold stone to not iretate same again.
        hold_nb = []    # temp hold all_nb for stone
        temp_nb.append(self)
        oX = self.x
        oY = self.y
            # Propagate the function to all connected neighbours
        def _feedforward(self, o_x, o_y, hold_nb):
            feed_hold = []
            feed_hold.append(self)
            # End of recursion
            if self.x == o_x and self.y == o_y:
                return feed_hold
            # add all connecting stones to _nb_all
            for nb in lnb:
                if nb not in temp_nb:
                    feed_hold.append(_feedforward(nb, oX, oY, hold_nb))
                else:
                    continue
            return feed_hold
        temp_nb.append(_feedforward(self, oX, oY, hold_nb))

        for i in temp_nb:
            print("\n")
            print(i)

    # Debug, print all neighbours
    def nb_all(self):
        if self.lnb is not None:
            for st in self.lnb:
                print('dicks')

a = st()
b = st()
c = st()
d = st()
a.pl(2,5)
b.pl(2,4)
c.pl(1,5)
d.pl(1,6)
a._iter()

class st_player:
    
    def __init__(self, color):
        
        if color == "b":
            self.STNUM = 181
        elif color == "w":
            self.STNUM = 180
        
        self.container = []
        for i in range(STNUM):
            self.container[i] = st()
    
    def pleasenamemelater(self):
        for st in self.container:
            if self.nb() is not None:
                for nb in self.nb():
                    print("asdasd")
                    #iterate   

    # iterate all objects in container
    # start a recursive string through all the objects to their neighbours
    # if string reaches entry point, it is complete.
    # complete string analyze the interior of the circle.
    # if container reaches the initial value, it is circle.







