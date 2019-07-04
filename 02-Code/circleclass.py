class Circle():

    
    def __init__(self,radius):
        self.radius=radius


    ###---------------Methods----------------####
    def area(self):
        pi=3.14
        
        print('Area of a circle is : {}'.format(self.radius*self.radius*pi))
    def circumfrance(self):
        pi=3.14
        print('Circumfrance of a Circle is : {} '.format(self.radius*pi*2))
    
n=int(input('enter no.'))
a=Circle(n)

a.area()
a.circumfrance()


class Maths():

    def __init__(self,number):
        self.number=number
    def square(self):
        print('Square of Number is : {}'.format(self.number*self.number))
    def cube(self):
        print('Cube of Number is : {}'.format(self.number*self.number*self.number))
    
b=int(input('enter no. '))
c= Maths(b)
c.square()
c.cube()
