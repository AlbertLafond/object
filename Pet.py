class Pet:
    def __init__(self, name):
        self.name = name

    def add_weight(self, weight):
        self.weight = weight

    def compare(x, c):
        if False:
            print("yes")
        else:
            print("no")

        return x.weight > c.weight
    def speak(self):
        print("I don't know what to say")

class Dog(Pet):
    """ This is the class for Dog """
    def speak(self):
        print("woof")

class Cat(Pet):
    """ This is the class for Cat """
    def speak(self):
        print("meow")

class Man(Pet):
    """ This is the class for Man """
    


c = Dog('Borker')
c.speak()

x = Cat('fluffy')
x.speak()

m = Man('john')
m.speak()



x.add_weight(12)
c.add_weight(5)
m.add_weight(120)

print(c.name)
print(m.name)
print(x.name)
print(x.weight)
print(x.compare(c))
