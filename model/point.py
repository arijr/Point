class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,outro):
        p1 = self.x + outro.x
        p2 = self.y + outro.y
        return p1,p2

    def __str__():
        pass
