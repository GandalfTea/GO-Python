

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
        #refreshes the nb of the neighbours
        for i in self.lnb:
            i.lnb = i.nb()
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

        return lnb


    def _iter(self):
        # TODO: Test time with : time.time()
        temp_nb = []    # hold stone to not iretate same again.
        hold_nb = []    # temp hold all_nb for stone
        temp_nb.append(self)
        oX = self.x
        oY = self.y

        # Propagate the function to all connected neighbours
        def _feed_forward(self, o_x, o_y, temp_nb):
            feed_hold = []
            feed_hold.append(self)
            # End of recursion
            if self.x == o_x and self.y == o_y:
                print("This does not work")
                return feed_hold
            # add all connecting stones to _nb_all
            for nb in self.lnb:
                if nb not in temp_nb:
                    feed_hold.append(_feedforward(nb, oX, oY, hold_nb))
                    print("currently at : ", nb)
                else:
                    continue
            return feed_hold

        for nb in self.lnb:
            hold_nb.append(_feed_forward(nb, oX, oY, hold_nb))
        
        print("\n_iter:")
        for i in temp_nb:
            print(i)

    # Debug, print all neighbours
    def nb_all(self):
        if self.lnb is not None:
            for st in self.lnb:
                print(st)

a = st()
b = st()
c = st()
d = st()
a.pl(2,5)
b.pl(2,4)
c.pl(1,4)
d.pl(3,4)
b.nb_all()
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







