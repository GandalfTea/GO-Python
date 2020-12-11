from stone_class import st


a = st()
a.pl(4,2)

b = st()
b.pl(3,2)

c = st()
c.pl(3,3)

d = st()
d.pl(4,3)
print(b._all_nb)
for i in b._all_nb:
    print(i)
