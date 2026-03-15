# Dunder methodes are the special methodes in python that start and end with double underscores, like __init__ , __str__ , __add__ etc.


# Example:-

class Person:
    def __init__(self , name):
        self.name = name 
p = Person("Ravi")
print(p.name)


class Animal:
    def __init__(self ,name , age):
        self.name = name 
        self.age = age 

    def __str__(self):
        return f"Hello how are you and your name is {self.name}"
    def __add__(self, other):
        return f"your sum of ages are {self.age + other.age}"
    
obj = Animal("Lion" , 12)
obj2 = Animal("Dolphin" ,14)
print(obj + obj2)

obj1 = Animal("Tiger" , 11)
print(obj1)