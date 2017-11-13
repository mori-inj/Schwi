class Outer(object):
    outerlist = []
    a = 2
    def __init__(self):
        pass
    class Inner(object):
        def __new__(self, arg1):
            Outer.outerlist.append(arg1)

f = Outer()
f.outerlist.append('A')
f.a = 3
f.Inner("apple")
f.Inner("orange")
print f.outerlist
print f.a
g = Outer()
g.outerlist = []
g.Inner("banana")
print g.outerlist
print g.a

print f.outerlist
print f.a
