from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass

    @abstractmethod
    def __str__(self): pass

class Square(Shape):    
    def __init__(self, edge):
        self.set_edge(edge)

    def get_edge(self):
        return self.__edge

    def set_edge(self, edge):
        if edge > 0:
            self.__edge = edge
        else:
            raise ValueError("Edge length must be positive!")

    def area(self):
        return self.__edge ** 2

    def perimeter(self):
        return self.__edge * 4

    def __str__(self):
        return f"Square: edge={self.__edge}, area={self.area()}, perimeter={self.perimeter()}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.set_dimensions(width, height)

    def get_dimensions(self):
        return self.__width, self.__height

    def set_dimensions(self, width, height):
        if width > 0 and height > 0:
            self.__width = width
            self.__height = height
        else:
            raise ValueError("Width and height must be positive!")

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    def __str__(self):
        return f"Rectangle: width={self.__width}, height={self.__height}, area={self.area()}, perimeter={self.perimeter()}"

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.set_sides(side1, side2, side3)

    def get_sides(self):
        return self.__side1, self.__side2, self.__side3

    def set_sides(self, side1, side2, side3):
        if side1 > 0 and side2 > 0 and side3 > 0 and (side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1):
            self.__side1 = side1
            self.__side2 = side2
            self.__side3 = side3
        else:
            raise ValueError("Invalid triangle sides! The sum of any two sides must be greater than the third side.")

    def area(self):
        s = (self.__side1 + self.__side2 + self.__side3) / 2
        return math.sqrt(s * (s - self.__side1) * (s - self.__side2) * (s - self.__side3))

    def perimeter(self):
        return self.__side1 + self.__side2 + self.__side3

    def __str__(self):
        return f"Triangle: sides=({self.__side1}, {self.__side2}, {self.__side3}), area={self.area():.2f}, perimeter={self.perimeter()}"

class Circle(Shape):
    PI = 3.14

    def __init__(self, radius):
        self.set_radius(radius)

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        if radius > 0:
            self.__radius = radius
        else:
            raise ValueError("Radius must be positive!")

    def area(self): 
        return Circle.PI * self.__radius ** 2

    def perimeter(self):
        return 2 * Circle.PI * self.__radius

    def __str__(self):
        return f"Circle: radius={self.__radius}, area={self.area()}, perimeter={self.perimeter()}"

# Function to get a positive number from the user
def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Error: Value must be positive!")
        except ValueError:
            print("Error: Please enter a valid number!")

# Get user input
radius = get_positive_float("Enter the circle's radius: ")
edge = get_positive_float("Enter the square's edge length: ")
width = get_positive_float("Enter the rectangle's width: ")
height = get_positive_float("Enter the rectangle's height: ")

print("\nEnter the sides of the triangle:")
while True:
    side1 = get_positive_float("Side 1: ")
    side2 = get_positive_float("Side 2: ")
    side3 = get_positive_float("Side 3: ")

    try:
        t = Triangle(side1, side2, side3)
        break
    except ValueError as e:
        print(f"Invalid triangle: {e}")
        print("Please enter valid triangle sides.")

# Create objects and display results
c = Circle(radius)
s = Square(edge)
r = Rectangle(width, height)

print("\nGenerated Objects:")
print(c)
print(s)
print(r)
print(t)
