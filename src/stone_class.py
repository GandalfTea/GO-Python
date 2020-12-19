from board import board

debug_buffer = []
debug_buffer.clear()

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
        self.lnb = []

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
        
        board[x][y] = self
        debug_buffer.append("\nStoned Played at : " + str((self.x, self.y)) + "\nColor : " + ("WHITE" if self.c=='w' else "BLACK"))
        _pl_st.append(self)
        self.deep_nb()      # Deep search neighbours, also close nb 

        # Refreshes the nb of the neighbours
        for i in self.lnb:
            i.deep_nb()



    # Get immediate nb of stone
    def nb(self):
        lnb = [] # List of neighbours
        if board[self.x][self.y - 1] is not None:
            lnb.append(board[self.x][self.y - 1])

        if board[self.x][self.y + 1] is not None:
            lnb.append(board[self.x][self.y + 1])

        if board[self.x - 1][self.y] is not None:
            lnb.append(board[self.x - 1][self.y])

        if board[self.x + 1][self.y] is not None:
            lnb.append(board[self.x + 1][self.y])

        self.lnb = lnb
        debug_buffer.append(str(self) + " : Close neighbour search successful.")
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

                # End of recursion 
                # Distance is the layer of nb.
                # stops immediate nb from detecting original stone.

                if self.lnb is None:
                    debug_buffer.append("ERROR : self.lnb is None")
                    return
                
                if not connected:
                    if o_pos in self.lnb and distance > 2:
                        #print("Connection confirmed for :", o_pos)
                        connected = True

                for nb in self.lnb:
                    if o_pos is not nb:

                        # Add all connecting stones to hold_nb
                        if nb.c == self.c:
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
            debug_buffer.append(str(self) + " : Deep neighbour search successful : _connected")
            debug_buffer.append("\tStatus : " + str(self.is_connected))
            for i in self._connected:
                debug_buffer.append("\t" + str(i))

            hold_newer.clear()

            for i in hold_all:
                if i not in self._all_nb:
                    if i is not self:
                        self._all_nb.append(i)
            debug_buffer.append(str(self) + " : Deep neighbour search successful : all_nb")

            for i in self._all_nb:
                debug_buffer.append("\t" + str(i))
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

