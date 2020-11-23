

allst = []
lnb = []

class st:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.nb()
        allst.append(self)
        print("string x :", x, "string y :", y)

    def nb(self):
       for st in allst:
           print("I will tel you a secreat.")
           if self.x == st.x or self.y == st.y or self.x == st.y or self.y == st.x:
                print("I was the wierd duck")
                lnb.append(st)

    def nb_all():
        for st in lnb:
            print(st.x, " ", st.y)

    # check neighbours
    # store neighbours if stones
    # if two similar coordinates, store in container.
    # if container reaches the initial value, it is circle.

a = st(3,4)
b = st(4,5)
st.nb_all()







