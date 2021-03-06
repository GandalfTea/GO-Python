

from board import board
import time

debug_buffer = [] # Buffer to transmit debug lines to the GUI.
debug_buffer.clear()

_all_st = []        #all stones
_pl_st = []         #played stones
_captured_st = []   # captured stones


class st:
    def __init__(self):
        self.x = 20             # Number outside the bounds of the board to prevent bugs.
        self.y = 20             # Same.
        self.lnb = []           # List of close neighbours (+- 1)
        self._all_nb = []       # All connected neighbours
        self._connected = []    # Hold all the stones in the connection (search for circles).
        self.is_connected = False
        self.c = ""             # Color

        _all_st.append(self)

    def __str__(self):
        if (self.x,self.y) in _pl_st or (self.x,self.y) in _captured_st:
            return "X : " + str(self.x) + ", Y : " + str(self.y)
        else:
            debug_buffer.append("ERROR : " + str(self) + " has not been played yet but there was an attempt to print it.")

    
    # Play a stone
    def pl(self, x, y):
        # Internal var, not important for play.
        self.x = x
        self.y = y

        board[x][y] = self  # Play stone
        _pl_st.append((self.x, self.y))

        debug_buffer.append("\nStoned Played at : " + str((self.x, self.y)) + "\nColor : " + ("WHITE" if self.c=='w' else "BLACK"))

        self.nb()           # Close neighbour search.
        self.deep_nb()      # Deep neighbour search.

        # Refreshes the nb of the neighbours
        debug_buffer.append("\nNeighbour refresh : ")
        for i in self.lnb:
            if i != 0:
                i.nb()
                i.deep_nb()



    # Get immediate nb of stone
    # If nb is 0, it is the edge of the board

    def nb(self):
        lnb = []
        if self.y-1 >= 0:
            if board[self.x][self.y - 1] is not None:
                lnb.append(board[self.x][self.y - 1])
        else:
            lnb.append(0)
        if self.y+1 < len(board):
            if board[self.x][self.y + 1] is not None:
                lnb.append(board[self.x][self.y + 1])
        else:
            lnb.append(0)

        if self.x-1 >= 0:
            if board[self.x - 1][self.y] is not None:
                lnb.append(board[self.x - 1][self.y])
        else:
            lnb.append(0)

        if self.x+1 < len(board):
            if board[self.x + 1][self.y] is not None:
                lnb.append(board[self.x + 1][self.y])
        else:
            lnb.append(0)



        # Bias the coming searches for the opposite color by putting it first:
        new_lnb=[]
        for a in lnb: 
            if a != 0 and a.c != self.c:
                new_lnb.append(a)
        for a in lnb: 
            if a not in new_lnb:
                new_lnb.append(a)

        self.lnb = new_lnb


        # Debug
        debug_buffer.append(str(self) + " : Close neighbour search successful.")
        for nb in new_lnb:
            debug_buffer.append("\t" + str(nb))

        return



    # Find connections between stones

    # Searches for 2 types of connection:
    #   1. Search for stones connected in a circle (until it reaches the original stone again) -> hold_connected.
    #   2. Search for groups of stones (all connected) -> hold_all.
    
    # Stones connected in a circle will be used to eventually count the score (not implemented). 

    def deep_nb(self):

        hold_connected = []     
        hold_all = []           
        o_pos = self

        # feed_forward branches into a tree search and if connected passed as argument, it will continue search even after True.
        global connected
        connected = False

        # Iterator that feeds forward the search to all nb of the same color.
        def _feed_forward(self, distance):
            global connected

            if self.lnb is None:
                debug_buffer.append("ERROR : self.lnb is None")
                return
            
            # End of recursion 
            # Distance is the layer of nb. Stops immediate nb from detecting original stone.
            if not connected:
                if o_pos in self.lnb and distance > 2:
                    connected = True

            for nb in self.lnb:

                # Skip edge of board
                if nb == 0:
                    continue

                # Add all connecting stones to hold_nb
                if o_pos is not nb:
                    if nb.c == self.c:
                        if nb not in hold_all:
                            if not connected : hold_connected.append(nb)
                            hold_all.append(nb)

                            new_dist = distance + 1
                            _feed_forward(nb, new_dist)

                            continue
                        else:
                            continue
            return 

        # Run iterator
        _feed_forward(self, 1)

        # Update connected (circular) stones.
        if connected:
            for i in hold_connected:
                i.is_connected = True


        # Add all found stones into respective container

        self._connected.clear()
        for i in hold_connected:
            self._connected.append(i)

        debug_buffer.append(str(self) + (" TRUE" if self.is_connected else " FALSE") +  " : Deep nb search successful : _connected")

        self._all_nb.clear()
        for i in hold_all:
            self._all_nb.append(i)


        debug_buffer.append(str(self) + " : Deep neighbour search successful : all_nb")
        for i in self._all_nb:
            debug_buffer.append("\t" + str(i))

    
        hold_all.clear()
        hold_connected.clear()



    # Checks to see if stone and nb are captured.

    # LOGIC : If all neighbours are occupied for all same color stones, than the group of stones or stone is captured.

    #   Iterate through the close neighbours:
    #        * if same color nb, propagate the search for nb to it and add original in container.
    #        * if there is no same color nb, captured.
    #   If not all nb are occupied, not captured.

    # RETURN : (color, number of stones captured, stone/s instances)

    def capture(self):

        # If not all the neighbours are occupies, return None.
        if len(self.lnb) != 4:
            debug_buffer.append(str(self) + " : Not enough neighbours for capture : " + str(len(self.lnb)))
            return None

        debug_buffer.append("Capture search engaged for : " + str(self))

        # Group capture search comes first to permit the use of eyes in the game.


        # Group capture search
        temp = []           # Hold stone to not iterate again.
        same_color = []     # Hold all captured stone to return.
        b_same_color = []   # Hold bool from iter() of same colored stones to check group capture.
        original_pos = self

        # If there are any same colored nb than commit to group search
        if any(nb == 0 or nb.c == self.c for nb in self.lnb):

            # If all nb are occupied, propagate the function to all same color nb and return True.
            def iter(self):
                # Update nb.
                self.nb()
                
                if len(self.lnb) != 4:
                    debug_buffer.append(str(self) + " : Not enough neighbours for group capture : " + str(len(self.lnb)))
                    return None

                temp.append(self)
                same_color.append(self)
                
                # Iterate through all same color stones.
                for nb in self.lnb:
                    if nb not in temp:
                        if nb == 0:
                            b_same_color.append(True)
                            continue
                        elif nb.c == self.c:
                            debug_buffer.append("Iterating : " + str(nb))
                            b_same_color.append(iter(nb))
                return True

            iter(self)

            # If all are captured, the group is captured.
            if len(same_color) > 0 and all(b_same_color):
                # Remove stones from board
                for st in same_color:
                    if (st.x,st.y) in _pl_st:
                        _pl_st.remove((st.x,st.y))
                    _captured_st.append((st.x,st.y))
                    board[st.x][st.y] = None

                debug_buffer.append("Group capture.")
                # Return stones so as to remove them from the GUI.

                return ('w' if str(same_color[0].c) == 'w' else 'b', len(same_color), same_color)
           
            else:
                debug_buffer.append("No capture found.")
                return None

        # Solo capture search
        else:      
            if all(nb == 0 or nb.c != self.c for nb in self.lnb):
                board[self.x][self.y] = None
                if (self.x,self.y) in _pl_st:
                    _pl_st.remove((self.x,self.y))
                _captured_st.append((self.x,self.y))
                debug_buffer.append("Solo capture")

                return ('w' if str(self.c) == 'w' else 'b',1, [self])
           
            else:
                return None


    def getColor(self):
        return self.c

    def getStatus(self):
        if (self.x, self.y) in _pl_st:
            return True
        else:
            return False
        


