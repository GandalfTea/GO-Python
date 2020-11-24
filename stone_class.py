

allst = []

class st:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.nb()
        self.lnb = self.nb()
        allst.append(self)
        print("string x :", x, "string y :", y)

    def nb(self):
        lnb = []
        for st in allst:
           #print("I will tel you a secreat.")
           if self.x == st.x or self.y == st.y or self.x == st.y or self.y == st.x:
                #print("I was the wierd duck")
                lnb.append(st)
        return lnb

    def nb_all(self):
        if self.lnb is not None:
            for st in self.lnb:
                print(st.x, " ", st.y)

    # if container reaches the initial value, it is circle.

a = st(3,4)
b = st(4,5)
c = st(4,6)
c.nb_all()





