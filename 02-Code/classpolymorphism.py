class Animal():

    def __init__(self,name):
        self.name = name

    def speak(self):
        raise(NotImplementedError)

class Dog(Animal):

    def speak(self):
        print(self.name + ' says Woof!')

class Cat(Animal):

    def speak(self):
        print(self.name + ' says Meow!')

D=Dog('Toomy')
C=Cat('sammy')
D.speak()
C.speak()
        
