class Line():

    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        c=coordinate2[0]-coordinate1[0]
        d=coordinate2[1]-coordinate1[1]
        dis=(((c**2)+(d**2)))**(1/2)
        return dis
    def slope(self):
        c=coordinate2[0]-coordinate1[0]
        d=coordinate2[1]-coordinate1[1]
        slp=d/c
        return slp

coordinate1=(3,2)
coordinate2=(8,10)
li = Line(coordinate1,coordinate2)
print(li.distance())
print(li.slope())

