
class Animal:

    def assignLegs(self, l):
        self.legs = l
    def amountOfLegs(self):
        return self.legs
    def setPredatorPrey(self, p):
        self.isPredatorPrey = p
    def getPredatorPrey(self):
        return self.isPredatorPrey
    def reactToAnimal(self, animal):
        if(animal.getPredatorPrey() == 'Predator' and self.getPredatorPrey() == 'Predator'):
            return ("The Predators dual it out!")
        elif(   (animal.getPredatorPrey() == 'Prey' and self.getPredatorPrey() == 'Predator')  or
                (animal.getPredatorPrey() == 'Predator' and self.getPredatorPrey() == 'Prey')
            ):
            # one animal is a predator and one is a prey
            return ("The Prey attemps to run away!")
        elif(animal.getPredatorPrey() == 'Prey' and self.getPredatorPrey() == 'Prey'):
            # both animals are prey
            return ("Both animals are docile.")
        else:
            # animal is undefined
            return ("This animal is yet to be discovered!")