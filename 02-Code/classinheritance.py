class Animal():
    def __init__(self):
        print('animal created')

    def who_am_i(self):
        print('I am an animal')
    def eat(self):
        print('I am eating')

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('khali hai')
    def who_am_i(self):
        print('pagal hun')

my_dog = Dog()
my_dog.eat()
my_dog.who_am_i()
