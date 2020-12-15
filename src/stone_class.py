
_all_st = []    #all stones
_pl_st = []     #played stones

class st:
    def __init__(self):
        self.x = 0
        self.y = 0
        self._all_nb = []
        self._connected = []
        self.is_connected = False
        self.c = ""

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
        self.nb()           # Find neighbours
        self.deep_nb()      # Deep search neighbours 
        # Refreshes the nb of the neighbours
        for i in self.lnb:
            i.lnb = i.nb()
            i.deep_nb()

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

        self.lnb = lnb
        return



    # Find connections between stones
    # TODO: Test time config
    def deep_nb(self):

        def _iter(self):
            hold_connected = []     # temp hold connected
            hold_all = []           # temp hold all connected
            o_pos = self            # Original stone position
            global connected
            connected = False

            #print("\nNow on:", self)

            # GOAL : Find stones connected in a circle
            # WORK : Iterate through neighbours until it finds the original stone
            def _feed_forward(self, distance):
                global connected
                self.nb()
                #print(self)
                # End of recursion 
                # Distance is the layer of nb.
                # stops immediate nb from detecting original stone.
                if not connected:
                    if o_pos in self.lnb and distance > 2:
                        #print("Connection confirmed for :", o_pos)
                        connected = True

                for nb in self.lnb:
                    if o_pos is not nb:
                        #print("\t", distance, nb)
                        #print("Status :", connected)
                        # Add all connecting stones to hold_nb
                        if nb not in hold_all:
                            if not connected : hold_connected.append(nb)
                            new_dist = distance + 1
                            hold_all.append(nb)
                            _feed_forward(nb, new_dist)
                            continue
                        else:
                            continue

                return 

            # Say that stone is connected
            _feed_forward(self, 1)
            if connected:
                for i in hold_connected:
                    i.is_connected = True


            # This is shit. Just cleaning my ass.
            # Add all found stones into respective container
            hold_newer = []

            for i in hold_connected:
                if i not in hold_newer:
                    if i is not self:
                        hold_newer.append(i)
            for i in hold_newer:
                if i not in self._connected:
                    self._connected.append(i)

            hold_newer.clear()

            for i in hold_all:
                if i not in self._all_nb:
                    if i is not self:
                        self._all_nb.append(i)

            hold_all.clear()
            hold_connected.clear()

        _iter(self)


    def getColor(self):
        return self.c
        
    # Debug, print all neighbours
    def nb_all(self):
        if self.lnb is not None:
            for st in self.lnb:
                print(st)


# BUNDLE :
# If all nb of one color are occupied, the bundle is captured
# Because if nb is black the bundle is bigger
# And if all nb occupied, it would eventually be white.

# If not all nb are occupied and all nb of unnocupied space are one color
# That is an eye.







