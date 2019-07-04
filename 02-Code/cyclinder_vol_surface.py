class Cyclinder():
    pi=3.14
    def __init__(self,height=1,radius=2):
        self.height = height
        self.radius = radius

    def volume(self):
        vol = self.pi*(self.radius**2)*self.height 
        return vol
    def surface_area(self):
        sur_area = 2*self.pi*self.radius*(self.height + self.radius)
        return sur_area


c = Cyclinder(2,3)
print(c.volume())
print(c.surface_area())

