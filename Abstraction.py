from abc import ABC , abstractmethod
class abstract(ABC):
    @abstractmethod
    def perimeter(self):
        pass
    @abstractmethod
    def area(self):
        pass
class Square(abstract):
    def __init__(self,side):
        self.side = side
class Circle(abstract):
    def __init__(self,radius):
        self.radius = radius
    
    def perimeter(self):
        print("I have created  perimeter")
    def area(self):
        print("I have created area also.")

obj = Circle(7)
obj2 = Square(12)

#syntax:-
# Importing ABC and abstractmethod
# from abc import ABC, abstractmethod

# # Creating an Abstract Class
# class Shape(ABC):

#     # Abstract method (only declared, not defined)
#     @abstractmethod
#     def area(self):
#         pass


# # Child class Rectangle
# class Rectangle(Shape):

#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     # Implementing abstract method
#     def area(self):
#         print("Area of Rectangle:", self.length * self.width)


# # Child class Circle
# class Circle(Shape):

#     def __init__(self, radius):
#         self.radius = radius

#     # Implementing abstract method
#     def area(self):
#         print("Area of Circle:", 3.14 * self.radius * self.radius)


# # Creating objects
# obj1 = Rectangle(10, 5)
# obj2 = Circle(7)

# # Calling methods
# obj1.area()
# obj2.area()