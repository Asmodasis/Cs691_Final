from Animal import Animal
class Dog(Animal):
    def __init__(self,l,p):
        self.assignLegs(l)
        self.setPredatorPrey(p)
    def bark(self):
        return("The dog barks.")

