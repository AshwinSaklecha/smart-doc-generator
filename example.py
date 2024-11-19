# Class 1: Dog
class Dog:
    """
    A class representing a dog with attributes like name and breed.
    Provides methods for dog actions like barking and fetching.
    """
    def __init__(self, name, breed):
        """
        Initializes a new Dog instance with a name and breed.
        
        Args:
        name (str): The dog's name.
        breed (str): The dog's breed.
        """
        self.name = name
        self.breed = breed

    def bark(self):
        """
        Makes the dog bark.

        Returns:
        str: The barking sound of the dog.
        """
        return f"{self.name} says Woof!"

    def fetch(self, item):
        """
        Makes the dog fetch an item.

        Args:
        item (str): The item to be fetched.

        Returns:
        str: A message indicating the dog fetched the item.
        """
        return f"{self.name} fetched the {item}!"

# Class 2: Owner
class Owner:
    """
    A class representing the owner of a dog.
    Provides methods for interacting with the dog, like playing and walking.
    """
    def __init__(self, name, dog):
        """
        Initializes a new Owner instance with a name and a dog.

        Args:
        name (str): The owner's name.
        dog (Dog): The Dog instance owned by this owner.
        """
        self.name = name
        self.dog = dog

    def play_with_dog(self):
        """
        Simulates playing with the dog by making it bark.

        Prints the owner's name and the dog's bark.
        """
        print(f"{self.name} is playing with {self.dog.name}.")
        print(self.dog.bark())

    def walk_dog(self):
        """
        Simulates walking the dog by printing related messages.

        Prints the owner's name and the dog's behavior.
        """
        print(f"{self.name} is walking with {self.dog.name}.")
        print(f"{self.dog.name} is wagging its tail.")

# Functions outside of classes
def greet_owner(owner_name):
    """
    Greets the owner with a welcome message.

    Args:
    owner_name (str): The name of the owner to greet.

    Returns:
    str: A greeting message for the owner.
    """
    return f"Hello, {owner_name}! Welcome to the park."

def dog_food(dog_breed):
    """
    Provides information about food based on the dog's breed.

    Args:
    dog_breed (str): The breed of the dog.

    Returns:
    str: A string indicating the type of food suitable for the dog.
    """
    if dog_breed.lower() == "beagle":
        return "Beagle food: Special mix of meats and vegetables."
    else:
        return "Dog food: Regular kibble."

def display_info(owner, dog):
    """
    Displays information about the owner and their dog.

    Args:
    owner (Owner): The owner instance.
    dog (Dog): The dog instance.

    Prints the owner's name, dog's name, and dog's breed.
    """
    print(f"Owner: {owner.name}, Dog: {dog.name}, Breed: {dog.breed}")
