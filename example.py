# Class 1: Dog
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!"

    def fetch(self, item):
        return f"{self.name} fetched the {item}!"

# Class 2: Owner
class Owner:
    def __init__(self, name, dog):
        self.name = name
        self.dog = dog

    def play_with_dog(self):
        print(f"{self.name} is playing with {self.dog.name}.")
        print(self.dog.bark())

    def walk_dog(self):
        print(f"{self.name} is walking with {self.dog.name}.")
        print(f"{self.dog.name} is wagging its tail.")

# Functions outside of classes
def greet_owner(owner_name):
    return f"Hello, {owner_name}! Welcome to the park."

def dog_food(dog_breed):
    if dog_breed.lower() == "beagle":
        return "Beagle food: Special mix of meats and vegetables."
    else:
        return "Dog food: Regular kibble."

def display_info(owner, dog):
    print(f"Owner: {owner.name}, Dog: {dog.name}, Breed: {dog.breed}")