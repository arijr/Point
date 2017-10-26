class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,outro):
        p1 = self.x + outro.x
        p2 = self.y + outro.y
        Pn = Point(p1,p2)

        return Pn
        # return self.__str__(p1,p2)

    def __str__(self): #__str__(self,p1,p2)

        return "Pn(%.2f,%.2f)"%(self.x,self.y)

        # return "Pn("+str(self.x)+","+str(self.y)+")"

    # def __str__(self,p1,p2):
    #     return "Pn("+str(p1)+","+str(p2)+")"

    # def __cmp__(self, outro):
    #     return cmp((self.x,self.y),(outro.x,outro.y))

    def __eq__(self, outro):
        return self.x == outro.x and self.y == outro.y
