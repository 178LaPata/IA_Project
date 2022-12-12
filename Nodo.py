
class Nodo:

    def __init__(self, x, y, velx, vely):
        self.x = x
        self.y = y
        self.velx = velx
        self.vely = vely

    def __str__(self):
        return f'({self.x},{self.y}),({self.velx},{self.vely})'

    def ___hash__(self):
        return hash(repr(self))

    def __eq__(self, other):
        if other is None or type(self) != type(other):
            return False
        return self.x==other.x and self.y==other.y and self.velx==other.velx and self.vely==other.vely

    def getPos(self):
        return [self.x,self.y]
    
    def getVel(self):
        return [self.velx,self.vely]
