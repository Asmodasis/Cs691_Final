
from Cat import Cat
from Dog import Dog
from Mouse import Mouse

if __name__ == "__main__":
    
    prey = None
    c = input("Please type first animal: [cat,dog,mouse]")
    if(c == "cat"):
        predator = Cat(4,"Predator")
        print(predator.meow())
    elif(c == "dog"):
        predator = Dog(4,"Predator")
        print(predator.bark())
    elif(c == "mouse"):
        prey = Mouse(4,"Prey")
        print(prey.squeak())
    else:
        print("Please select a valid first animal.")

    d = input("Please type second animal: [cat,dog,mouse]")
    if(d == "cat"):
        predator2 = Cat(4,"Predator")
        print(predator2.meow())
    elif(d == "dog"):
        predator2 = Dog(4,"Predator")
        print(predator2.bark())
    elif(d == "mouse"):
        prey = Mouse(4,"Prey")
        print(prey.squeak())
    else:
        print("Please select a valid second animal.")
    
    if(prey is not None):
        print(prey.reactToAnimal(predator))
    else:
        print(predator2.reactToAnimal(predator))
