

_all_st = []    #all stones
_pl_st = []     #played stones

class st:
    def __init__(self):
        self.x = 0
        self.y = 0
        self._all_nb = []

        _all_st.append(self)

    def pl(self, x, y):
        self.x = x
        self.y = y
        self.lnb = self.nb()
        _pl_st.append(self)
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
        temp_nb = []    # hold stone to not iretate same again.
        hold_nb = []    # temp hold all_nb for stone
        temp_nb.append(self)
           
            # Propagate the function to all connected neighbours
            def _feedforward(self, o_x, o_y, hold_nb):
                feed_hold = []
                if self.x == o_x and self.y == o_y:
                    return 

                # add all connecting stones to _nb_all
                for nb in lnb:
                    if nb not in temp_nb:
                        feed_hold.append(nb)
                    else:
                        continue
                return feed_hold

    # Debug, print all neighbours
    def nb_all(self):
        if self.lnb is not None:
            for st in self.lnb:


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







