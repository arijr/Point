class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,outro):
        p1 = self.x + outro.x
        p2 = self.y + outro.y
        return self.__str__(p1,p2)

    def __str__(self,p1,p2):
        return "Pn("+str(p1)+","+str(p2)+")"
