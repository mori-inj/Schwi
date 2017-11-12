from sets import Set
from types import *

# http://geocoq.github.io/GeoCoq/html/GeoCoq.Axioms.euclidean_axioms.html

class Geo:
    names = {}
    conds = Set([])
    conclusion = []
    
    def __init__(self):
        pass
    
    class Point:
        def __init__(self, s):
            assert type(s) is StringType, 'name should be string'
            assert s not in Geo.names, 'name is already being used'
            self.name = s
            Geo.names[s] = self
            Geo.conds.add(Geo.Eq(s,s))
        def __str__(self):
            return 'Point ' + self.name

    class Circle:
        def __init__(self, s):
            assert type(s) is StringType, 'name should be string'
            assert s not in Geo.names, 'name is already being used'
            self.name = s
            Geo.names[s] = self
        def __str__(self):
            return 'Circle ' + self.name



    """====Conditions===="""

    class Cong:
        def __init__(self, A, B, C, D): # p0,p1,p2,p3 := dist(p0,p1) == dist(p2,p3)
            self.A = A
            self.B = B
            self.C = C
            self.D = D
            Geo.conds.add(self)
        def __hash__(self):
            return hash(self.__class__) ^ (hash(self.A)<<1) ^ (hash(self.B)<<2) ^ (hash(self.C)<<3) ^ (hash(self.D)<<4)
        def __eq__(self, other):
            return self.__hash__() == other.__hash__()
        def __str__(self):
            return self.A + self.B + " == " + self.C + self.D

    class BetS:
        def __init__(self, A, B, C): # p0,p1,p2 := p0*p1*p2
            self.A = A
            self.B = B
            self.C = C
            Geo.conds.add(self)
        def __hash__(self):
            return hash(self.__class__) ^ (hash(self.A)<<1) ^ (hash(self.B)<<2) ^ (hash(self.C)<<3)
        def __eq__(self, other):
            return self.__hash__() == other.__hash__()
        def __str__(self):
            return self.A + " * " + self.B + " * " + self.C
    
    class nBetS:
        def __init__(self, A, B, C): # p0,p1,p2 := p0*p1*p2
            self.A = A
            self.B = B
            self.C = C
            Geo.conds.add(self)
        def __hash__(self):
            return hash(self.__class__) ^ (hash(self.A)<<1) ^ (hash(self.B)<<2) ^ (hash(self.C)<<3)
        def __eq__(self, other):
            return self.__hash__() == other.__hash__()
        def __str__(self):
            return "! " + self.A + " * " + self.B + " * " + self.C


    class InCirc: # p,c := dist(c.o,p) < c.r
        def __init__(self, P, C):
            self.P = P
            self.C = C
            Geo.conds.add(self)
        def __hash__(self):
            return hash(self.__class__) ^ (hash(self.P)<<1) ^ (hash(self.C)<<2)
        def __eq__(self, other):
            return self.__hash__() == other.__hash__()
        def __str__(self):
            return self.P + " is in circle " + self.C

    class OnCirc: # p,c := dist(c.o,p) == c.r
        def __init__(self, P, C):
            self.P = P
            self.C = C
            Geo.conds.add(self)
        def __hash__(self):
            return hash(self.__class__) ^ (hash(self.P)<<1) ^ (hash(self.C)<<2)
        def __eq__(self, other):
            return self.__hash__() == other.__hash__()
        def __str__(self):
            return self.P + " is on circle " + self.C

    class OutCirc: # p,c := dist(c.o,p) > c.r
        def __init__(self, P, C):
            self.P = P
            self.C = C
            Geo.conds.add(self)
        def __hash__(self):
            return hash(self.__class__) ^ (hash(self.P)<<1) ^ (hash(self.C)<<2)
        def __eq__(self, other):
            return self.__hash__() == other.__hash__()
        def __str__(self):
            return self.P + " is out of circle " + self.C


    class CI:
        def __init__(self, O, P, A, B): # c,p0,p1,p2 := { c.o := p0, c.r := dist(p1,p2) }
            self.O = O
            self.P = P
            self.A = A
            self.B = B
            Geo.conds.add(self)
        def __hash__(self):
            return hash(self.__class__) ^ (hash(self.O)<<1) ^ (hash(self.P)<<2) ^ (hash(self.A)<<3) ^ (hash(self.B)<<4)
        def __eq__(self, other):
            return self.__hash__() == other.__hash__()
        def __str__(self):
            return "There exists Circle " + self.O + ", with origin " + self.P + " and radius " + self.A + self.B

    class Eq:
        def __init__(self, A, B): # p0,p1 := p0 == p1
            assert A in Geo.names, 'point not defined'
            assert B in Geo.names, 'point not defined'
            self.A = A
            self.B = B
            Geo.conds.add(self)
        def __hash__(self):
            return hash(self.__class__) ^ (hash(self.A)<<1) ^ (hash(self.B)<<1)
        def __eq__(self, other):
            return self.__hash__() == other.__hash__()
        def __str__(self):
            return self.A + " == " + self.B
    
    class nEq:
        def __init__(self, A, B): # p0,p1 := p0 != p1
            assert A in Geo.names, 'point not defined'
            assert B in Geo.names, 'point not defined'
            self.A = A
            self.B = B
            Geo.conds.add(self)
        def __hash__(self):
            return hash(self.__class__) ^ (hash(self.A)<<1) ^ (hash(self.B)<<1)
        def __eq__(self, other):
            return self.__hash__() == other.__hash__()
        def __str__(self):
            return self.A + " != " + self.B

    class TE:
        def __init__(self, A, B, C): # p0,p1,p2 := !(p0!=p1 & p1!=p2 & !(p0*p1*p2))
            assert A in Geo.names, 'point not defined'
            assert B in Geo.names, 'point not defined'
            assert C in Geo.names, 'point not defined'
            self.A = A
            self.B = B
            self.C = C
            Geo.conds.add(self)
        def __hash__(self):
            return hash(self.__class__) ^ (hash(self.A)<<1) ^ (hash(self.B)<<2) ^ (hash(self.C)<<3)
        def __eq__(self, other):
            return self.__hash__() == other.__hash__()

    class nCol:
        def __init__(self, A, B, C): # p0,p1,p2 := (p0!=p1 & p0!=p2 & p1!=p2 & !(p0*p1*p2) & !(p0*p2*p1) & !(p1*p0*p2))
            assert A in Geo.names, 'point not defined'
            assert B in Geo.names, 'point not defined'
            assert C in Geo.names, 'point not defined'
            self.A = A
            self.B = B
            self.C = C
            Geo.conds.add(self)
        def __hash__(self):
            return hash(self.__class__) ^ (hash(self.A)<<1) ^ (hash(self.B)<<2) ^ (hash(self.C)<<3)
        def __eq__(self, other):
            return self.__hash__() == other.__hash__()

    class Col:
        def __init__(self, A, B, C): # p0,p1,p2 := !nCol p0,p1,p2
            assert A in Geo.names, 'point not defined'
            assert B in Geo.names, 'point not defined'
            assert C in Geo.names, 'point not defined'
            self.A = A
            self.B = B
            self.C = C
            Geo.conds.add(self)
        def __hash__(self):
            return hash(self.__class__) ^ (hash(self.A)<<1) ^ (hash(self.B)<<2) ^ (hash(self.C)<<3)
        def __eq__(self, other):
            return self.__hash__() == other.__hash__()

    class Cong3:
        def __init__(self, A, B, C, a, b, c):
            assert A in Geo.names, 'point not defined'
            assert B in Geo.names, 'point not defined'
            assert C in Geo.names, 'point not defined'
            assert a in Geo.names, 'point not defined'
            assert b in Geo.names, 'point not defined'
            assert c in Geo.names, 'point not defined'
            self.A = A
            self.B = B
            self.C = C
            self.a = a
            self.b = b
            self.c = c
            Geo.conds.add(self)
        def __hash__(self):
            return hash(self.__class__) ^ (hash(self.A)<<1) ^ (hash(self.B)<<2) ^ (hash(self.C)<<3) \
                    ^ (hash(self.a)<<4) ^ (hash(self.b)<<5) ^ (hash(self.c)<<6)
        def __eq__(self, other):
            return self.__hash__() == other.__hash__()

    """class TS:
        def __init__(self, P, A, B, Q)"""

    class Triangle:
        def __init__(self, A, B, C): # p0,p1,p2 := (p0!=p1 & p0!=p2 & p1!=p2 & !(p0*p1*p2) & !(p0*p2*p1) & !(p1*p0*p2))
            assert A in Geo.names, 'point not defined'
            assert B in Geo.names, 'point not defined'
            assert C in Geo.names, 'point not defined'
            self.A = A
            self.B = B
            self.C = C

            size = len(Geo.conds)
            nAB = Geo.nEq(A,B)
            if len(Geo.conds) > size:
                Geo.conds.remove(nAB)
            nBC = Geo.nEq(B,C)
            if len(Geo.conds) > size:
                Geo.conds.remove(nBC)
            nAC = Geo.nEq(A,C)
            if len(Geo.conds) > size:
                Geo.conds.remove(nAC)
            nABC = Geo.nBetS(A,B,C)
            if len(Geo.conds) > size:
                Geo.conds.remove(nABC)
            nACB = Geo.nBetS(A,C,B)
            if len(Geo.conds) > size:
                Geo.conds.remove(nACB)
            nBAC = Geo.nBetS(B,A,C)
            if len(Geo.conds) > size:
                Geo.conds.remove(nBAC)
            
            assert nAB in Geo.conds and nBC in Geo.conds and nAC in Geo.conds \
                    and nABC in Geo.conds and nACB in Geo.conds and nBAC in Geo.conds, 'insufficient conditions'
            Geo.conds.add(self)
        def __hash__(self):
            return hash(self.__class__) ^ (hash(self.A)<<1) ^ (hash(self.B)<<2) ^ (hash(self.C)<<3)
        def __eq__(self, other):
            return self.__hash__() == other.__hash__()
        def __str__(self):
            return 'Triangle '+ self.A + self.B + self.C

    
    
    """====Axioms===="""

    def eq_trans(self, A, B, C):
        assert A in Geo.names, 'point not defined'
        assert B in Geo.names, 'point not defined'
        assert C in Geo.names, 'point not defined'
        assert Geo.names[A].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[B].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[C].__class__.__name__ is 'Point', 'given type is not point'
        
        size = len(Geo.conds)
        AB = Geo.Eq(A,B)
        if len(Geo.conds) > size:
            Geo.conds.remove(AB)
        BC = Geo.Eq(B,C)
        if len(Geo.conds) > size:
            Geo.conds.remove(BC)
        assert AB in Geo.conds, A+'=='+B+' not satisfied'
        assert BC in Geo.conds, B+'=='+C+' not satisfied'

        Geo.conds.add(Geo.Eq(A,C))
    
    def cong_trans(self, A, B, C, D, P, Q):
        assert A in Geo.names, 'point not defined'
        assert B in Geo.names, 'point not defined'
        assert C in Geo.names, 'point not defined'
        assert D in Geo.names, 'point not defined'
        assert P in Geo.names, 'point not defined'
        assert Q in Geo.names, 'point not defined'
        assert Geo.names[A].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[B].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[C].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[D].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[P].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[Q].__class__.__name__ is 'Point', 'given type is not point'
        
        size = len(Geo.conds)
        PQ_AB = Geo.Cong(P,Q, A,B)
        if len(Geo.conds) > size:
            Geo.conds.remove(PQ_AB)
        PQ_CD = Geo.Cong(P,Q, C,D)
        if len(Geo.conds) > size:
            Geo.conds.remove(PQ_CD)
        assert PQ_AB in Geo.conds, P+Q+'=='+A+B+' not satisfied'
        assert PQ_CD in Geo.conds, P+Q+'=='+C+D+' not satisfied'

        Geo.conds.add(Geo.Cong(A,B, C,D))

    def eq_refl(self, A):
        assert A in Geo.names, 'point not defined'
        assert Geo.names[A].__class__.__name__ is 'Point', 'given type is not point'
        
        Geo.conds.add(Geo.Eq(A,A))

    def cong_refl(self, A, B):
        assert A in Geo.names, 'point not defined'
        assert B in Geo.names, 'point not defined'
        assert Geo.names[A].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[B].__class__.__name__ is 'Point', 'given type is not point'
        
        Geo.conds.add(Geo.Cong(A,B, A,B))

    def eq_rev(self, A, B):
        assert A in Geo.names, 'point not defined'
        assert B in Geo.names, 'point not defined'
        assert Geo.names[A].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[B].__class__.__name__ is 'Point', 'given type is not point'
        
        Geo.conds.add(Geo.Cong(A,B, B,A))

    # def stab(self, A, B):

    def eq_sub(self, A, B, C, D):
        assert A in Geo.names, 'point not defined'
        assert B in Geo.names, 'point not defined'
        assert C in Geo.names, 'point not defined'
        assert D in Geo.names, 'point not defined'
        assert Geo.names[A].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[B].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[C].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[D].__class__.__name__ is 'Point', 'given type is not point'

        size = len(Geo.conds)
        DA = Geo.Eq(D,A)
        if len(Geo.conds) > size:
            Geo.conds.remove(DA)
        ABC = Geo.BetS(A,B,C)
        if len(Geo.conds) > size:
            Geo.conds.remove(ABC)

        assert DA in Geo.conds, D+'=='+A+' not satisfied'
        assert ABC in Geo.conds, A+'*'+B+'*'+C+' not satisfied'

        Geo.conds.add(Geo.BetS(D,B,C))

    def circle(self, A, B, C, O):
        assert A in Geo.names, 'point not defined'
        assert B in Geo.names, 'point not defined'
        assert C in Geo.names, 'point not defined'
        assert Geo.names[A].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[B].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[C].__class__.__name__ is 'Point', 'given type is not point'
        assert O not in Geo.names, 'name is already being used'

        size = len(Geo.conds)
        AB = Geo.nEq(A,B)
        if len(Geo.conds) > size:
            Geo.conds.remove(AB)

        assert AB in Geo.conds, A+'!='+B+' not satisfied'

        Geo.Circle(O)
        Geo.conds.add(Geo.CI(O, C, A,B))

    def inside_circle(self, A, B, C, J, P, X=None, Y=None):
        assert (X is None and Y is None) or (X is not None and Y is not None)
        if X is None and Y is None:
            assert A in Geo.names, 'point not defined'
            assert B in Geo.names, 'point not defined'
            assert C in Geo.names, 'point not defined'
            assert P in Geo.names, 'point not defined'
            assert J in Geo.names, 'circle not defined'
            assert Geo.names[A].__class__.__name__ is 'Point', 'given type is not point'
            assert Geo.names[B].__class__.__name__ is 'Point', 'given type is not point'
            assert Geo.names[C].__class__.__name__ is 'Point', 'given type is not point'
            assert Geo.names[P].__class__.__name__ is 'Point', 'given type is not point'
            assert Geo.names[J].__class__.__name__ is 'Circle', 'given type is not circle'

            size = len(Geo.conds)
            J_CI = Geo.CI(J, C, A,B)
            if len(Geo.conds) > size:
                Geo.conds.remove(J_CI)

            assert J_CI in Geo.conds, 'circle with given origin and radius is not defined'
            
            sat = False
            for nameX in Geo.names:
                X = Geo.names[nameX]
                if X.__class__.__name__ is 'Point':
                    for nameY in Geo.names:
                        Y = Geo.names[nameY]
                        if Y.__class__.__name__ is 'Point' and Y is not X:
                            XCY = Geo.BetS(nameX,C,nameY)
                            if len(Geo.conds) > size:
                                Geo.conds.remove(XCY)
                            CY_AB = Geo.Cong(C,nameY, A,B)
                            if len(Geo.conds) > size:
                                Geo.conds.remove(CY_AB)
                            CX_AB = Geo.Cong(C,nameX, A,B)
                            if len(Geo.conds) > size:
                                Geo.conds.remove(CX_AB)
                            XPY = Geo.BetS(nameX,P,nameY)
                            if len(Geo.conds) > size:
                                Geo.conds.remove(XPY)
                            
                            if XCY in Geo.conds and CY_AB in Geo.conds and CX_AB in Geo.conds and XPY in Geo.conds:
                                sat = True
                                break
                if sat:
                    break
                            
            assert sat, 'insufficient conditions'
            Geo.conds.add(Geo.InCirc(P, J))
        else:
            assert A in Geo.names, 'point not defined'
            assert B in Geo.names, 'point not defined'
            assert C in Geo.names, 'point not defined'
            assert P in Geo.names, 'point not defined'
            assert J in Geo.names, 'circle not defined'
            assert Geo.names[A].__class__.__name__ is 'Point', 'given type is not point'
            assert Geo.names[B].__class__.__name__ is 'Point', 'given type is not point'
            assert Geo.names[C].__class__.__name__ is 'Point', 'given type is not point'
            assert Geo.names[P].__class__.__name__ is 'Point', 'given type is not point'
            assert Geo.names[J].__class__.__name__ is 'Circle', 'given type is not circle'
            assert X not in Geo.names, 'name is already being used'
            assert Y not in Geo.names, 'name is already being used'

            size = len(Geo.conds)
            J_CI = Geo.CI(J, C, A,B)
            if len(Geo.conds) > size:
                Geo.conds.remove(J_CI)
            PinJ = Geo.InCirc(P,J)
            if len(Geo.conds) > size:
                Geo.conds.remove(PinJ)

            assert J_CI in Geo.conds, 'circle with given origin and radius is not defined'
            assert PinJ in Geo.conds, '\"'+P+' is in '+J+'\" not satisfied'

            Geo.Point(X)
            Geo.Point(Y)
            Geo.BetS(X,C,Y)
            Geo.Cong(C,Y, A,B)
            Geo.Cong(C,X, A,B)
            Geo.BetS(X,P,Y)

    def outside_circle(self, A, B, C, J, P, X=None):
        if X is None:
            assert A in Geo.names, 'point not defined'
            assert B in Geo.names, 'point not defined'
            assert C in Geo.names, 'point not defined'
            assert P in Geo.names, 'point not defined'
            assert J in Geo.names, 'circle not defined'
            assert Geo.names[A].__class__.__name__ is 'Point', 'given type is not point'
            assert Geo.names[B].__class__.__name__ is 'Point', 'given type is not point'
            assert Geo.names[C].__class__.__name__ is 'Point', 'given type is not point'
            assert Geo.names[P].__class__.__name__ is 'Point', 'given type is not point'
            assert Geo.names[J].__class__.__name__ is 'Circle', 'given type is not circle'

            size = len(Geo.conds)
            J_CI = Geo.CI(J, C, A,B)
            if len(Geo.conds) > size:
                Geo.conds.remove(J_CI)
            
            assert J_CI in Geo.conds, 'circle with given origin and radius is not defined'
                    
            sat = False
            for nameX in Geo.names:
                X = Geo.names[nameX]
                if X.__class__.__name__ is 'Point':     
                    CXP = Geo.BetS(C,nameX,P)
                    if len(Geo.conds) > size:
                        Geo.conds.remove(CXP)
                    CX_AB = Geo.Cong(C,nameX, A,B)
                    if len(Geo.conds) > size:
                        Geo.conds.remove(CX_AB)

                    if CXP in Geo.conds and CX_AB in Geo.conds:
                        sat = True
                        break

            assert sat, 'insufficient conditions'
            Geo.conds.add(Geo.OutCirc(P, J))
        else:
            assert A in Geo.names, 'point not defined'
            assert B in Geo.names, 'point not defined'
            assert C in Geo.names, 'point not defined'
            assert P in Geo.names, 'point not defined'
            assert J in Geo.names, 'circle not defined'
            assert Geo.names[A].__class__.__name__ is 'Point', 'given type is not point'
            assert Geo.names[B].__class__.__name__ is 'Point', 'given type is not point'
            assert Geo.names[C].__class__.__name__ is 'Point', 'given type is not point'
            assert Geo.names[P].__class__.__name__ is 'Point', 'given type is not point'
            assert Geo.names[J].__class__.__name__ is 'Circle', 'given type is not circle'
            assert X not in Geo.names, 'name is already being used'

            size = len(Geo.conds)
            J_CI = Geo.CI(J, C, A,B)
            if len(Geo.conds) > size:
                Geo.conds.remove(J_CI)
            PoutJ = Geo.OutCirc(P,J)
            if len(Geo.conds) > size:
                Geo.conds.remove(PoutJ)

            assert J_CI in Geo.conds, 'circle with given origin and radius is not defined'
            assert PoutJ in Geo.conds, '\"P is not in J\" not satisfied'

            Geo.Point(X)
            Geo.BetS(C,X,P)
            Geo.Cong(C,X, A,B)

    def on_circle(self, A, B, C, D, J):
        assert A in Geo.names, 'point not defined'
        assert B in Geo.names, 'point not defined'
        assert C in Geo.names, 'point not defined'
        assert D in Geo.names, 'point not defined'
        assert J in Geo.names, 'circle not defined'
        assert Geo.names[A].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[B].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[C].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[D].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[J].__class__.__name__ is 'Circle', 'given type is not circle'

        size = len(Geo.conds)
        J_CI = Geo.CI(J, A, C,D)
        if len(Geo.conds) > size:
            Geo.conds.remove(J_CI)
        AB_CD = Geo.Cong(A,B, C,D)
        if len(Geo.conds) > size:
            Geo.conds.remove(AB_CD)
        BonJ = Geo.OnCirc(B,J)
        if len(Geo.conds) > size:
            Geo.conds.remove(BonJ)

        assert J_CI in Geo.conds, 'circle with given origin and radius is not defined'
        assert AB_CD in Geo.conds or BonJ in Geo.conds, 'neither satisfies'
        if AB_CD in Geo.conds:
            Geo.conds.add(Geo.OnCirc(B, J))
        if BonJ in Geo.conds:
            Geo.conds.add(Geo.Cong(A,B, C,D))


    def bet_id(self, A, B):
        assert A in Geo.names, 'point not defined'
        assert B in Geo.names, 'point not defined'
        assert Geo.names[A].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[B].__class__.__name__ is 'Point', 'given type is not point'
        Geo.conds.add(Geo.nBetS(A,B,A))

    def bet_sym(self, A, B, C):
        assert A in Geo.names, 'point not defined'
        assert B in Geo.names, 'point not defined'
        assert C in Geo.names, 'point not defined'
        assert Geo.names[A].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[B].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[C].__class__.__name__ is 'Point', 'given type is not point'

        size = len(Geo.conds)
        ABC = Geo.BetS(A,B,C)
        if len(Geo.conds) > size:
            Geo.conds.remove(ABC)

        assert ABC in Geo.conds, 'insufficient conditions'
        Geo.conds.add(Geo.BetS(C,B,A))

    def inner_trans(self, A, B, C, D):
        assert A in Geo.names, 'point not defined'
        assert B in Geo.names, 'point not defined'
        assert C in Geo.names, 'point not defined'
        assert D in Geo.names, 'point not defined'
        assert Geo.names[A].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[B].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[C].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[D].__class__.__name__ is 'Point', 'given type is not point'

        size = len(Geo.conds)
        ABD = Geo.BetS(A,B,D)
        if len(Geo.conds) > size:
            Geo.conds.remove(ABD)
        BCD = Geo.BetS(B,C,D)
        if len(Geo.conds) > size:
            Geo.conds.remove(BCD)

        assert ABD in Geo.conds and BCD in Geo.conds, 'insufficient conditions'
        Geo.conds.add(Geo.BetS(A,B,C))

    def connectivity(self, A, B, C, D):
        assert A in Geo.names, 'point not defined'
        assert B in Geo.names, 'point not defined'
        assert C in Geo.names, 'point not defined'
        assert D in Geo.names, 'point not defined'
        assert Geo.names[A].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[B].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[C].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[D].__class__.__name__ is 'Point', 'given type is not point'

        size = len(Geo.conds)
        ABD = Geo.BetS(A,B,D)
        if len(Geo.conds) > size:
            Geo.conds.remove(ABD)
        ACD = Geo.BetS(A,C,D)
        if len(Geo.conds) > size:
            Geo.conds.remove(ACD)
        nABC = Geo.nBetS(A,B,C)
        if len(Geo.conds) > size:
            Geo.conds.remove(nABC)
        nACB = Geo.nBetS(A,C,B)
        if len(Geo.conds) > size:
            Geo.conds.remove(nACB)

        assert ABD in Geo.conds and ACD in Geo.conds and nABC in Geo.conds and nACB in Geo.conds, 'insufficient conditions'
        Geo.conds.add(Geo.Eq(B,C))

    def null_seg1(self, A, B, C):
        assert A in Geo.names, 'point not defined'
        assert B in Geo.names, 'point not defined'
        assert C in Geo.names, 'point not defined'
        assert Geo.names[A].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[B].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[C].__class__.__name__ is 'Point', 'given type is not point'

        size = len(Geo.conds)
        AB_CC = Geo.Cong(A,B, C,C)
        if len(Geo.conds) > size:
            Geo.conds.remove(AB_CC)

        assert AB_CC in Geo.conds, 'insufficient conditions'
        Geo.conds.add(Geo.Eq(A,B))

    def null_seg2(self, A, B):
        assert A in Geo.names, 'point not defined'
        assert B in Geo.names, 'point not defined'
        assert Geo.names[A].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[B].__class__.__name__ is 'Point', 'given type is not point'

        Geo.conds.add(Geo.Cong(A,A, B,B))

    def null_seg3(self, A, B, C, D):
        assert A in Geo.names, 'point not defined'
        assert B in Geo.names, 'point not defined'
        assert C in Geo.names, 'point not defined'
        assert D in Geo.names, 'point not defined'
        assert Geo.names[A].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[B].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[C].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[D].__class__.__name__ is 'Point', 'given type is not point'

        size = len(Geo.conds)
        nAB = Geo.nEq(A,B)
        if len(Geo.conds) > size:
            Geon.conds.remove(nAB)
        AB_CD = Geo.Cong(A,B, C,D)
        if len(Geo.conds) > size:
            Geo.conds.remove(AB_CD)

        assert nAB in Geo.conds and AB_CD in Geo.conds, 'insufficient conditions'
        Geo.conds.add(Geo.nEq(C,D)) 

    def five_line(self, A, B, C, D, a, b, c, d):
        assert A in Geo.names, 'point not defined'
        assert B in Geo.names, 'point not defined'
        assert C in Geo.names, 'point not defined'
        assert D in Geo.names, 'point not defined'
        assert a in Geo.names, 'point not defined'
        assert b in Geo.names, 'point not defined'
        assert c in Geo.names, 'point not defined'
        assert d in Geo.names, 'point not defined'
        assert Geo.names[A].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[B].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[C].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[D].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[a].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[b].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[c].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[d].__class__.__name__ is 'Point', 'given type is not point'

        size = len(Geo.conds)
        BC_bc = Geo.Cong(B,C, b,c)
        if len(Geo.conds) > size:
            Geo.conds.remove(BC_bc)
        AD_ad = Geo.Cong(A,D, a,d)
        if len(Geo.conds) > size:
            Geo.conds.remove(AD_ad)
        BD_bd = Geo.Cong(B,D, b,d)
        if len(Geo.conds) > size:
            Geo.conds.remove(BD_bd)
        ABC = Geo.BetS(A,B,C)
        if len(Geo.conds) > size:
            Geo.conds.remove(ABC)
        abc = Geo.BetS(a,b,c)
        if len(Geo.conds) > size:
            Geo.conds.remove(abc)
        AB_ab = Geo.Cong(A,B, a,b)
        if len(Geo.conds) > size:
            Geo.conds.remove(AB_ab)

        assert BC_bc in Geo.conds and AD_ad in Geo.conds and BD_bd in Geo.conds \
                and ABC in Geo.conds and abc in Geo.conds and AB_ab in Geo.conds, 'insufficient conditions'
        Geo.conds.add(Geo.Cong(D,C, d,c))

    def ext1(self, A, B, C, D, X):
        assert A in Geo.names, 'point not defined'
        assert B in Geo.names, 'point not defined'
        assert C in Geo.names, 'point not defined'
        assert D in Geo.names, 'point not defined'
        assert Geo.names[A].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[B].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[C].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[D].__class__.__name__ is 'Point', 'given type is not point'
        assert X not in Geo.names, 'name is already being used'

        size = len(Geo.conds)
        nAB = Geo.nEq(A,B)
        if len(Geo.conds) > size:
            Geo.conds.remove(nAB)
        nCD = Geo.nEq(C,D)
        if len(Geo.conds) > size:
            Geo.conds.remove(nCD)

        assert nAB in Geo.conds and nCD in Geo.conds, 'insufficient conditions'

        Geo.Point(X)
        Geo.BetS(A,B,X)
        Geo.Cong(B,X, C,D)

    def ext2(self, A, B, C, D, X):
        assert A in Geo.names, 'point not defined'
        assert B in Geo.names, 'point not defined'
        assert C in Geo.names, 'point not defined'
        assert D in Geo.names, 'point not defined'
        assert Geo.names[A].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[B].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[C].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[D].__class__.__name__ is 'Point', 'given type is not point'
        assert X not in Geo.names, 'name is already being used'

        size = len(Geo.conds)
        nAB = Geo.nEq(A,B)
        if len(Geo.conds) > size:
            Geo.conds.remove(nAB)
        
        assert nAB in Geo.conds, 'insufficient conditions'

        Geo.Point(X)
        Geo.TE(A,B,X)
        Geo.Cong(B,X, C,D)

    def pasch_inner(self, A, B, C, P, Q, X):
        assert A in Geo.names, 'point not defined'
        assert B in Geo.names, 'point not defined'
        assert C in Geo.names, 'point not defined'
        assert P in Geo.names, 'point not defined'
        assert Q in Geo.names, 'point not defined'
        assert Geo.names[A].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[B].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[C].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[P].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[Q].__class__.__name__ is 'Point', 'given type is not point'
        assert X not in Geo.names, 'name is already being used'
        
        size = len(Geo.conds)
        APC = Geo.BetS(A,P,C)
        if len(Geo.conds) > size:
            Geo.conds.remove(APC)
        BQC = Geo.BetS(B,Q,C)
        if len(Geo.conds) > size:
            Geo.conds.remove(BQC)
        ACB = Geo.nCol(A,C,B)
        if len(Geo.conds) > size:
            Geo.conds.remove(ACB)

        assert APC in Geo.conds and BQC in Geo.conds and ACB in Geo.conds, 'insufficient conditions'

        Geo.Point(X)
        Geo.BetS(A,X,Q)
        Geo.BetS(B,X,P)

    def pasch_outer(self, A, B, C, P, Q, X):
        assert A in Geo.names, 'point not defined'
        assert B in Geo.names, 'point not defined'
        assert C in Geo.names, 'point not defined'
        assert P in Geo.names, 'point not defined'
        assert Q in Geo.names, 'point not defined'
        assert Geo.names[A].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[B].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[C].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[P].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[Q].__class__.__name__ is 'Point', 'given type is not point'
        assert X not in Geo.names, 'name is already being used'
        
        size = len(Geo.conds)
        APC = Geo.BetS(A,P,C)
        if len(Geo.conds) > size:
            Geo.conds.remove(APC)
        BCQ = Geo.BetS(B,C,Q)
        if len(Geo.conds) > size:
            Geo.conds.remove(BCQ)
        BQA = Geo.nCol(B,Q,A)
        if len(Geo.conds) > size:
            Geo.conds.remove(BQA)

        assert APC in Geo.conds and BCQ in Geo.conds and BQA in Geo.conds, 'insufficient conditions'

        Geo.Point(X)
        Geo.BetS(A,X,Q)
        Geo.BetS(B,P,X)


    def line_circle(self, A, B, C, K, P, Q, X, Y):
        assert A in Geo.names, 'point not defined'
        assert B in Geo.names, 'point not defined'
        assert C in Geo.names, 'point not defined'
        assert P in Geo.names, 'point not defined'
        assert Q in Geo.names, 'point not defined'
        assert K in Geo.names, 'circle not defined'
        assert Geo.names[A].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[B].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[C].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[P].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[Q].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[K].__class__.__name__ is 'Circle', 'given type is not circle'
        assert X not in Geo.names, 'name is already being used'
        assert Y not in Geo.names, 'name is already being used'

        size = len(Geo.conds)
        K_CI = Geo.CI(K, C, P,Q)
        if len(Geo.conds) > size:
            Geo.conds.remove(K_CI)
        BK = Geo.InCirc(B,K)
        if len(Geo.conds) > size:
            Geo.conds.remove(BK)
        nAB = Geo.nEq(A,B)
        if len(Geo.conds) > size:
            Geo.conds.remove(nAB)

        assert K_CI in Geo.conds and BK in Geo.conds and nAB in Geo.conds, 'insufficient conditions'

        Geo.Point(X)
        Geo.Point(Y)
        Geo.Col(A,B,X)
        Geo.Col(A,B,Y)
        Geo.OnCirc(X,K)
        Geo.OnCirc(Y,K)
        Geo.BetS(X,B,Y)

    def circle_circle(self, C, D, F, G, J, K, P, Q, R, S, X):
        assert C in Geo.names, 'point not defined'
        assert D in Geo.names, 'point not defined'
        assert F in Geo.names, 'point not defined'
        assert G in Geo.names, 'point not defined'
        assert J in Geo.names, 'circle not defined'
        assert K in Geo.names, 'circle not defined'
        assert P in Geo.names, 'point not defined'
        assert Q in Geo.names, 'point not defined'
        assert R in Geo.names, 'point not defined'
        assert S in Geo.names, 'point not defined'
        assert Geo.names[C].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[D].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[F].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[G].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[J].__class__.__name__ is 'Circle', 'given type is not circle'
        assert Geo.names[K].__class__.__name__ is 'Circle', 'given type is not circle'
        assert Geo.names[P].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[Q].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[R].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[S].__class__.__name__ is 'Point', 'given type is not point'
        assert X not in Geo.names, 'name is already being used'

        size = len(Geo.conds)
        J_CI = Geo.CI(J, C, R,S)
        if len(Geo.conds) > size:
            Geo.conds.remove(J_CI)
        PJ = Geo.InCirc(P,J)
        if len(Geo.conds) > size:
            Geo.conds.remove(PJ)
        QJ = Geo.OutCirc(Q,J)
        if len(Geo.conds) > size:
            Geo.conds.remove(QJ)
        K_CI = Geo.CI(K, D, F,G)
        if len(Geo.conds) > size:
            Geo.conds.remove(K_CI)
        PK = Geo.OnCirc(P,K)
        if len(Geo.conds) > size:
            Geo.conds.remove(PK)
        QK = Geo.OnCirc(Q,K)
        if len(Geo.conds) > size:
            Geo.conds.remove(QK)

        assert J_CI in Geo.conds and PJ in Geo.conds and QJ in Geo.conds \
                and K_CI in Geo.conds and PK in Geo.conds and QK in Geo.conds, 'insufficient conditions'

        Geo.Point(X)
        Geo.OnCirc(X,J)
        Geo.OnCirc(X,K)

    def euclid5(self, a, p, q, r, s, t, X):
        assert a in geo.names, 'point not defined'
        assert p in geo.names, 'point not defined'
        assert q in geo.names, 'point not defined'
        assert r in geo.names, 'point not defined'
        assert s in geo.names, 'point not defined'
        assert t in geo.names, 'point not defined'
        assert Geo.names[a].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[p].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[q].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[r].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[s].__class__.__name__ is 'Point', 'given type is not point'
        assert Geo.names[t].__class__.__name__ is 'Point', 'given type is not point'
        assert X not in Geo.names, 'name is already being used'

        size = len(Geo.conds)
        rts = Geo.BetS(r,t,s)
        if len(Geo.conds) > size:
            Geo.conds.remove(rts)
        ptq = Geo.BetS(p,t,q)
        if len(Geo.conds) > size:
            Geo.conds.remove(ptq)
        raq = Geo.BetS(r,a,q)
        if len(Geo.conds) > size:
            Geo.conds.remove(raq)
        pt_qt = Geo.Cong(p,t, q,t)
        if len(Geo.conds) > size:
            Geo.conds.remove(pt_qt)
        tr_ts = Geo.Cong(t,r, t,s)
        if len(Geo.conds) > size:
            Geo.conds.remove(tr_ts)
        pqs = Geo.nCol(p,q,s)
        if len(Geo.conds) > size:
            Geo.conds.remove(pqs)

        assert rts in Geo.conds and ptq in Geo.conds and raq in Geo.conds \
                and pt_qt in Geo.conds and tr_ts in Geo.conds and pqs in Geo.conds, 'insufficient conditions'
        
        Geo.Point(X)
        Geo.BetS(p,a,X)
        Geo.BetS(s,q,X)



    """====lemma===="""
    def lem_cong_sym(self, A, B, C, D):
        self.cong_refl(B,C)
        self.cong_trans(A,D,B,C,B,C)

    def lem_cong_trans(self, A, B, C, D, E, F):
        self.lem_cong_sym(C,A,B,D)
        self.cong_trans(A,B,E,F,C,D)

    def lem_3_5b(self, A, B, C, D):
        self.inner_trans(A,B,C,D)
        self.lem_3_7a(A,B,C,D)

    def lem_3_6a(self, A, B, C, D):
        self.bet_sym(A,B,C)
        self.bet_sym(A,C,D)
        self.inner_trans(D,C,B,A)
        self.bet_sym(B,C,D)

    def lem_3_6b(self, A, B, C, D):
        self.bet_sym(A,B,C)
        self.bet_sym(A,C,D)
        self.lem_3_5b(A,B,C,D)
   
    def lem_3_7a(self, A, B, C, D):
        self.lem_bet_not_eq(A,B,C)
        self.lem_bet_not_eq(B,C,D)
        self.ext1(A,C,C,D,'lem_3_7a')
        self.cong_refl(C,'lem_3_7a')
        self.lem_cong_sym(C,'lem_3_7a',C,D)
        self.lem_3_6a(A,B,C,'lem_3_7a')
        self.lem_ext_uniq(B,C,D,'lem_3_7a')
        self.bet_sym(A,C,E)
        self.eq_sub(E,C,A,D)
        self.bet_sym(D,C,A)

    def lem_ext_uniq(self, A, B, E, F):
        self.lem_bet_not_eq(A,B,E)
        self.cong_refl(B,E)
        self.lem_cong_sym(B,B,E,F)
        self.cong_refl(A,E)
        self.cong_refl(A,B)
        self.lem_cong_sym(B,B,F,E)
        self.five_line(A,B,E,E,A,B,F,E)
        self.lem_cong_sym(E,E,E,F)
        self.null_seg1(E,F,E)

    def lem_bet_not_eq(self, A, B, C): # should be proven
        size = len(Geo.conds)
        ABC = Geo.BetS(A,B,C)
        if len(Geo.conds) > size:
            Geo.conds.remove(ABC)
        assert ABC in Geo.conds, A+'*'+B+'*'+C+' not satisfied'

        Geo.conds.add(Geo.nEq(A,B))
        Geo.conds.add(Geo.nEq(B,C))
        Geo.conds.add(Geo.nEq(A,C))

    def lem_part_not_eq_whole(self, A, B, C):
        pass


    def contrapos_lem_part_not_eq_whole(self, A, B, C):
        size = len(Geo.conds)
        AB_AC = Geo.Cong(A,B, A,C)
        if len(Geo.conds) > size:
            Geo.conds.remove(AB_AC)
        assert AB_AC in Geo.conds, A+B+' == '+A+C+' not satisfied'

        Geo.conds.add(Geo.nBetS(A,B,C))



    """====def===="""
    class equilateral:
        def __init__(self, A, B, C):
            assert A in Geo.names, 'point not defined'
            assert B in Geo.names, 'point not defined'
            assert C in Geo.names, 'point not defined'
            self.A = A
            self.B = B
            self.C = C

            size = len(Geo.conds)
            AB_BC = Geo.Cong(A,B, B,C)
            if len(Geo.conds) > size:
                Geo.conds.remove(AB_BC)
            BC_CA = Geo.Cong(B,C, C,A)
            if len(Geo.conds) > size:
                Geo.conds.remove(B,C, C,A)

            assert AB_BC in Geo.conds and BC_CA in Geo.conds, 'insufficient conditinos'
            Geo.conds.add(self)

        def __hash__(self):
            return hash(self.__class__) ^ (hash(self.A)<<1) ^ (hash(self.B)<<2) ^ (hash(self.C)<<3)
        def __eq__(self, other):
            return self.__hash__() == other.__hash__()
        def __str__(self):
            return A+B+' == '+B+C +' /\ '+B+C+' == '+C+A




    """====Conclusion===="""
    def SetConclusion(self, *args):
        self.conclusion = args


    def CheckConclusion(self):
        print ">>======================="
        for c in self.conclusion:
            size = len(self.names)+len(self.conds)
            try:
                exec 'tmp = Geo.' + c
                if len(self.names) + len(self.conds) > size:
                    if tmp in self.conds:
                        self.conds.remove(tmp)
                    elif tmp.name in self.names:
                        del self.names[tmp.name]
                    break
                else:
                    print c
            except:
                print c
        else:
            print 'QED.'



        




G = Geo()

G.Point('A')
G.Point('B')
G.nEq('A','B')

G.SetConclusion("Point('C')", "equilateral('A','B','C')", "Triangle('A','B','C')")
#G.CheckConclusion()

G.circle('A','B','A','J') # CI(J A AB)
G.circle('A','B','B','K') # CI(K B AB)
G.ext1('B','A','A','B','D')
G.eq_rev('B','A')
G.outside_circle('A','B','B','K','D') # OutCirc(D, K)
G.ext1('A','B','A','B','E')
G.inside_circle('A','B','B','K','B') # InCirc(B, K)
G.on_circle('A','D','A','B','J')
G.cong_refl('A','B')
G.on_circle('A','B','A','B','J')
#G.CheckConclusion()
G.circle_circle('B','A','A','B','K','J','B','D','A','B','C')
G.on_circle('A','C','A','B','J')
G.lem_cong_sym('A','A','C','B')
G.on_circle('B','C','A','B','K')
G.lem_cong_trans('B','C','A','B','A','C')
G.lem_cong_sym('A','B','C','B')
G.eq_rev('A','C')
G.lem_cong_trans('B','C','A','C','C','A')
#for cond in G.conds:
#    print str(cond)

G.null_seg3('A','B','B','C')
G.null_seg3('B','C','C','A')

#G.CheckConclusion()

G.contrapos_lem_part_not_eq_whole('A','C','B')
G.contrapos_lem_part_not_eq_whole('A','B','C')
G.lem_cong_trans('B','A','A','B','B','C')
G.contrapos_lem_part_not_eq_whole('B','A','C')
G.equilateral('A','B','C')
#G.CheckConclusion()
G.Triangle('A','B','C')

#for cond in G.conds:
#    print str(cond)

G.CheckConclusion()
