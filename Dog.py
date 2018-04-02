class Dog:
    """ This is the class for Dog """
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
        



c = Dog('Borker')

x = Dog('Woofer')

x.add_weight(12)

c.add_weight(19)

print(c.name)

print(x.name)
print(x.weight)
print(x.compare(c))
