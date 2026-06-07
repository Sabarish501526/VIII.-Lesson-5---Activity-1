from abc import ABC, abstractmethod

# ----- Abstract Base Class (Parent) ------------------
# Animal inherits from ABC - This makes it an abstract class (Abstraction)
class Animal(ABC):

    # Parent constructor - stores attributes shared by all animals
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    # Concrete method - all child classes inherit this for free
    def display(self):
        print(f"Name: {self.name}  |  Habitat: {self.habitat}")

    # Abstract method - every child class MUST implement this
    @abstractmethod
    def speak(self):
        pass
        
# ---- CHILD CLASS 1 ------------------------------
class Dog(Animal):

    def __init__(self, name, habitat, breed):
        super().__init__(name, habitat)   # calls Animal's constructor
        self.breed = breed

    def speak(self):
        print(f"{self.name} ({self.breed}) says: Woof! Woof!")


# ---- CHILD CLASS 2 ------------------------------
class Parrot(Animal):

    def __init__(self, name, habitat, phrase):
        super().__init__(name, habitat)
        self.phrase = phrase

    def speak(self):
        print(f"{self.name} says: {self.phrase}! {self.phrase}!")


# ---- CHILD CLASS 3 ------------------------------
class Lion(Animal):

    def __init__(self, name, habitat, pride):
        super().__init__(name, habitat)
        self.pride = pride

    def speak(self):
        print(f"{self.name} (Pride: {self.pride}) says: ROARRR!")


# ---- CREATE OBJECT & RUN THE SHOW ----------------
dog = Dog("Bruno", "Home", "Labrador")
parrot = Parrot("Polly", "Jungle", "Squawk")
lion = Lion("Simba", "Savannah", "Pride Rock")

print("=== Animals Sound Show")
for animal in [dog, parrot, lion]:
    animal.display()
    animal.speak()
    print()
        