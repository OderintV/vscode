class Animal:
    def eat(self):
        print("Animal can eat")
    def sleep(self):
        print("Animal can sleep")

class Bird(Animal):
    def fly(self):
        print("Birds can fly")

my_bird = Bird()
my_bird.eat()
my_bird.sleep()
my_bird.fly()

