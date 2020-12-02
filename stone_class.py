

allst = []
plst = []

class st:
    def __init__(self):
        self.x = 0
        self.y = 0
        self._all_nb = []

        allst.append(self)

    def pl(self, x, y):
        self.x = x
        self.y = y
        self.lnb = self.nb()
        plst.append(self)
        allst.append(self)
        #print("string x :", x, "string y :", y)

    def nb(self):
        lnb = []
        for st in allst:
           #print("I will tel you a secreat.")
           # TODO : This does not capture neighbours 
           if self.x == st.x or self.y == st.y or self.x == st.y or self.y == st.x:
                #print("I was the wierd duck")
                lnb.append(st)
        return lnb


    def _iter(self):
        temp_nb = []    # hold stone to not iretate same again.
        hold_nb = []    # temp hold all_nb for stone
        temp_nb.append(self)
            
        # iter ending function     
        for temp in temp_np:
            if self.x == temp.x and self.y == temp.y:
                # return

        # add all connecting stones to _nb_all
        for nb in lnb:
            if nb not in temp_nb:
                hold_nb.append(nb.iter())
            else:
                return nb

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







