class Dog:

    def _init_(self, name):
        self.name + name

    def add_weight(self, weight):
        self.weight = weight


c = Dog('Borker')
# c.name = 'Borker'

x = Dog('Woofer')
# x.name = 'Woofer'

x.add_weight(12)
# x.add_weight(12)

print(c.name)

print(x.name)
print(x.weight)
