from Animal import Animal
class Mouse(Animal):
    def __init__(self,l,p):
        self.assignLegs(l)
        self.setPredatorPrey(p)
    def squeak(self):
        return("The mouse squeaks.")
