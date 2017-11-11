from sets import Set

S = Set([])

class A:
    def __init__(self, x, y):
        self.x = x;
        self.y = y;
    def __hash__(self):
        return hash(self.x) ^ hash(self.y)
    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

class B:
    def __init__(self, x):
        self.x = x;
    def __hash__(self):
        return hash(self.x)
    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

a = A(1,2);
b = A(1,2);

S.add(a)
print(a.__hash__())
print(b.__hash__())
print(a==b)
print(b in S)
S.add(b)
print(S)
