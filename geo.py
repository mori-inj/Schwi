from sets import Set
from types import *

class Geo:
    names = {}
    conds = Set([])
    
    def __init__(self):
        pass
    
    class point:
        def __init__(self, s):
            assert type(s) is StringType, 'name should be string'
            assert s not in Geo.names, 'name is already being used'
            self.name = s
            Geo.names[s] = self

    class circle:
        def __init__(self, s):
            assert type(s) is StringType, 'name should be string'
            assert s not in Geo.names, 'name is already being used'
            self.name = s
            Geo.names[s] = self

    class Cong:
        def __init__(self, A, B, C, D): # p0,p1,p2,p3 := dist(p0,p1) == dist(p2,p3)
            self.A = A
            self.B = B
            self.C = C
            self.D = D
            Geo.conds.add(self)
        def __hash__(self):
            return hash(self.__class__) ^ hash(self.A) ^ hash(self.B) ^ hash(self.C) ^ hash(self.D)
        def __eq__(self, other):
            return self.__hash__() == other.__hash__()

    class BetS:
        def __init__(self, A, B, C): # p0,p1,p2 := p0*p1*p2
            self.A = A
            self.B = B
            self.C = C
            Geo.conds.add(self)
        def __hash__(self):
            return hash(self.__class__) ^ hash(self.A) ^ hash(self.B) ^ hash(self.C)
        def __eq__(self, other):
            return self.__hash__() == other.__hash__()

    class InCirc: # p,c := dist(c.o,p) < c.r
        def __init__(self, P, C):
            self.P = P
            self.C = C
            Geo.conds.add(self)
        def __hash__(self):
            return hash(self.__class__) ^ hash(self.P) ^ hash(self.C)
        def __eq__(self, other):
            return self.__hash__() == other.__hash__()

    class OnCirc: # p,c := dist(c.o,p) == c.r
        def __init__(self, P, C):
            self.P = P
            self.C = C
            Geo.conds.add(self)
        def __hash__(self):
            return hash(self.__class__) ^ hash(self.P) ^ hash(self.C)
        def __eq__(self, other):
            return self.__hash__() == other.__hash__()

    class OutCirc: # p,c := dist(c.o,p) > c.r
        def __init__(self, P, C):
            self.P = P
            self.C = C
            Geo.S.add(self)
        def __hash__(self):
            return hash(self.__class__) ^ hash(self.P) ^ hash(self.C)
        def __eq__(self, other):
            return self.__hash__() == other.__hash__()

    class Circle:
        def __init__(self, O, P, A, B): # c,p0,p1,p2 := { c.o := p0, c.r := dist(p1,p2) }
            self.O = O
            self.P = P
            self.A = A
            self.B = B
            Geo.conds.add(self)
        def __hash__(self):
            return hash(self.__class__) ^ hash(self.O) ^ hash(self.P) ^ hash(self.A) ^ hash(self.B)
        def __eq__(self, other):
            return self.__hash__() == other.__hash__()

    class eq:
        def __init__(self, A, B): # p0,p1 := p0 == p1
            self.A = A
            self.B = B
            Geo.conds.add(self)
        def __hash__(self):
            return hash(self.__class__) ^ hash(self.A) ^ hash(self.B)
        def __eq__(self, other):
            return self.__hash__() == other.__hash__()
    
    class neq:
        def __init__(self, A, B): # p0,p1 := p0 != p1
            self.A = A
            self.B = B
            Geo.conds.add(self)
        def __hash__(self):
            return hash(self.__class__) ^ hash(self.A) ^ hash(self.B)
        def __eq__(self, other):
            return self.__hash__() == other.__hash__()

    class TE:
         def __init__(self, A, B, C): # p0,p1,p2 := !(p0!=p1 & p1!=p2 & !(p0*p1*p2))
            self.A = A
            self.B = B
            self.C = C
            Geo.conds.add(self)
        def __hash__(self):
            return hash(self.__class__) ^ hash(self.A) ^ hash(self.B) ^ hash(self.C)
        def __eq__(self, other):
            return self.__hash__() == other.__hash__()

    class nCol:
         def __init__(self, A, B, C): # p0,p1,p2 := !(p0!=p1 & p1!=p2 & !(p0*p1*p2))
            self.A = A
            self.B = B
            self.C = C
            Geo.conds.add(self)
        def __hash__(self):
            return hash(self.__class__) ^ hash(self.A) ^ hash(self.B) ^ hash(self.C)
        def __eq__(self, other):
            return self.__hash__() == other.__hash__()

    class Col:
         def __init__(self, A, B, C): # p0,p1,p2 := !(p0!=p1 & p1!=p2 & !(p0*p1*p2))
            self.A = A
            self.B = B
            self.C = C
            Geo.conds.add(self)
        def __hash__(self):
            return hash(self.__class__) ^ hash(self.A) ^ hash(self.B) ^ hash(self.C)
        def __eq__(self, other):
            return self.__hash__() == other.__hash__()





