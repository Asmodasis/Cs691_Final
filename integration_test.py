from Cat import Cat
from Dog import Dog
from Mouse import Mouse


def test_cat_react_to_dog(cat, dog):
        assert (cat.reactToAnimal(dog) == "The Predators dual it out!")

def test_cat_react_to_mouse(cat, mouse):
        assert (cat.reactToAnimal(mouse) == "The Prey attemps to run away!")
        
def test_dog_react_to_cat(dog, cat):
        assert (dog.reactToAnimal(cat) == "The Predators dual it out!")
        
def test_dog_react_to_mouse(dog, mouse):
        assert (dog.reactToAnimal(mouse) == "The Prey attemps to run away!")
        
def test_mouse_react_to_cat(mouse, cat):
        assert (mouse.reactToAnimal(cat) == "The Prey attemps to run away!")
        
def test_mouse_react_to_dog(mouse, dog):
        assert (mouse.reactToAnimal(dog) == "The Prey attemps to run away!")
        

if __name__ == "__main__":
    cat = Cat(4,"Predator")
    dog = Dog(4,"Predator")
    mouse = Mouse(4,"Prey")
    test_cat_react_to_dog(cat,dog)
    test_cat_react_to_mouse(cat,mouse)
    test_dog_react_to_cat(dog,cat)
    test_dog_react_to_mouse(dog,mouse)
    test_mouse_react_to_cat(mouse,cat)
    test_mouse_react_to_dog(mouse,dog)