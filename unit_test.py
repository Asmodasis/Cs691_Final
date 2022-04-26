
from Cat import Cat
from Dog import Dog
from Mouse import Mouse

def unit_test_animal_predator_prey(animal, test_predator_prey="Not Defined"):
        animal.setPredatorPrey(test_predator_prey)
        assert (animal.getPredatorPrey() == test_predator_prey)

def unit_test_animal_legs(animal, amount_of_legs=2):
        animal.assignLegs(amount_of_legs)
        assert (animal.amountOfLegs() == amount_of_legs)

def unit_test_cat(cat):
        assert (cat.meow() == "The cat meows.")

def unit_test_dog(dog):
        assert (dog.bark() == "The dog barks.")

def unit_test_mouse(mouse):
        assert (mouse.squeak() == "The mouse squeaks.")

if __name__ == "__main__":
    
    cat = Cat(4,"Predator")
    dog = Dog(4,"Predator")
    mouse = Mouse(4,"Prey")

    unit_test_animal_predator_prey(cat)
    unit_test_animal_legs(cat)
    unit_test_animal_predator_prey(dog, "Predator")
    unit_test_animal_legs(dog, 4)

    unit_test_cat(cat)
    unit_test_dog(dog)
    unit_test_mouse(mouse)
 