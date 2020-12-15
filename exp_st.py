from stone_class import st


a = st()
a.pl(4,2)

b = st()
b.pl(3,2)

c = st()
c.pl(3,3)

d = st()
d.pl(4,3)

e = st()
e.pl(5,2)

f = st()
f.pl(5,3)
f.deep_nb()
print("\n")
for i in f._all_nb:
    print(i)
print("\n")
for i in f._connected:
    print(i)
