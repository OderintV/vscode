class Animal:
    def speak(self):
        print("animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

def make_animal_speak(Animal):
    Animal.speak()

a = Animal()
d = Dog()
make_animal_speak(a)
make_animal_speak(d)

