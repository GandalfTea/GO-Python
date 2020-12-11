

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

    # Play a stone
    def pl(self, x, y):
        self.x = x
        self.y = y
        _pl_st.append(self)
        self.lnb = self.nb() # Find neighbours
        self._iter()         # Deep search neighbours 
        # Refreshes the nb of the neighbours
        for i in self.lnb:
            i.lnb = i.nb()
            i._iter()

    # Get immediate nb of stone
    def nb(self):
        lnb = [] # List of neighbours
        for st in _all_st:
            if st.x == self.x and st.y == (self.y - 1):
                lnb.append(st)
            elif st.x == self.x and st.y == (self.y + 1):
                lnb.append(st)
            elif st.x == (self.x - 1) and st.y == self.y:
                lnb.append(st)
            elif st.x == (self.x + 1) and st.y == self.y:
                lnb.append(st)
            else:
                continue

        return lnb


    # This function is the stuff of nightmares.

    # It is recursive through all neighbours until it finds
    # the first stone again, creating a circle.
    # TODO: Test time config
    
    def _iter(self):
        temp_nb = []    # hold stone to not iretate same again.
        hold = []    # temp hold all_nb for original stone
        o_pos = [self.x, self.y]    # Original stone position

        # Propagate the function to all connected neighbours
        def _feed_forward(self, o_pos, distance, hold_nb):

            if o_pos != [self.x, self.y]: 
                if self not in temp_nb:
                    temp_nb.append(self)
                
                    # Add all connecting stones to hold_nb
                    for nb in self.lnb:
                        new_dist = distance + 1
                        if nb not in hold_nb:
                            hold_nb.append(nb)
                        _feed_forward(nb, o_pos, new_dist, hold_nb)

            else:
                # End of recursion 
                # Distance is the layer of nb.
                # Stops immediate nb from detecting original stone.
                if distance == 1:
                    temp_nb.append(self)
                else:
                    print("Connection confirmed.")
                    return

        # Add all found stones into original stone's _all_nb
        for nb in self.lnb:
            _feed_forward(nb, o_pos, 1, hold)
        self._all_nb.append(hold)
        
    # Debug, print all neighbours
    def nb_all(self):
        if self.lnb is not None:
            for st in self.lnb:
                print(st)


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







