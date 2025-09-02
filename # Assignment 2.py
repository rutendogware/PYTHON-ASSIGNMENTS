# Assignment 2
#
#


#QUESTION 1
# Base class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def describe(self):
        return f"This is a vehicle: {self.brand} {self.model}"


# Subclass Car
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def describe(self):
        return f"This is a car: {self.brand} {self.model} with {self.doors} doors"


# Subclass Bike
class Bike(Vehicle):
    def __init__(self, brand, model, type_of_bike):
        super().__init__(brand, model)
        self.type_of_bike = type_of_bike

    def describe(self):
        return f"This is a {self.type_of_bike} bike: {self.brand} {self.model}"


# Example usage
v = Vehicle("Generic", "Model-X")
c = Car("Toyota", "Corolla", 4)
b = Bike("Yamaha", "MT-07", "sport")

print(v.describe())  # Output: This is a vehicle: Generic Model-X
print(c.describe())  # Output: This is a car: Toyota Corolla with 4 doors
print(b.describe())  # Output: This is a sport bike: Yamaha MT-07




#QUESTION 2
import math

# Base class
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")


# Circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


# Rectangle class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Function to calculate total area using polymorphism
def total_area(shapes):
    return sum(shape.area() for shape in shapes)


# Example usage
shapes = [
    Circle(5),             # Area ≈ 78.54
    Rectangle(4, 6),       # Area = 24
    Circle(2.5),           # Area ≈ 19.63
    Rectangle(3, 7)        # Area = 21
]

print(f"Total area: {total_area(shapes):.2f}")




#QUESTION 3
# Base class
class Shape:
    def __init__(self, name="Shape"):
        self.name = name
        print(f"Shape initialized: {self.name}")

    def calculate_area(self):
        print("Calculating area in Shape (placeholder)")
        return 0


# Derived class
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(name="Rectangle")  # Call Shape's __init__
        self.width =




#QUESTION 4
# Define the Dog class
class Dog:
    def make_sound(self):
        return "Woof!"


# Define the Cat class
class Cat:
    def make_sound(self):
        return "Meow!"


# Function that uses polymorphism
def process_sound(sound_object):
    sound = sound_object.make_sound()
    print(f"Sound made: {sound}")


# Example usage
dog = Dog()
cat = Cat()

process_sound(dog)  # Output: Sound made: Woof!
process_sound(cat)  # Output: Sound made: Meow!




#QUESTION 5
from abc import ABC, abstractmethod

# Abstract base class
class FileHandler(ABC):
    @abstractmethod
    def read(self, filepath):
        pass

    @abstractmethod
    def write(self, filepath, data):
        pass

# Concrete class for handling text files
class TextFileHandler(FileHandler):
    def read(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        return content

    def write(self, filepath, data):
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(data)

# Concrete class for handling binary files
class BinaryFileHandler(FileHandler):
    def read(self, filepath):
        with open(filepath, 'rb') as file:
            content = file.read()
        return content

    def write(self, filepath, data):
        with open(filepath, 'wb') as file:
            file.write(data)

# Example usage (would normally be in a different script or test)
if __name__ == "__main__":
    text_handler = TextFileHandler()
    text_handler.write('example.txt', 'Hello, World!')
    print(text_handler.read('example.txt'))

    binary_handler = BinaryFileHandler()
    binary_handler.write('example.bin', b'\x00\x01\x02')
    print(binary_handler.read('example.bin'))
