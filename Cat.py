from Animal import Animal
class Cat(Animal):
    def __init__(self,l,p):
        self.assignLegs(l)
        self.setPredatorPrey(p)
    def meow(self):
        return("The cat meows.")
