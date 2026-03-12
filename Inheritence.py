class Factorymumbai:   #Parent class/superclass/ 
    a = 'I am an attribute mentioned inside Factory'
    def hello(self):
        print("Hello , I am a method inside Factory")

class Factorypune(Factorymumbai):   #child class 
    pass   
obj = Factorymumbai()

obj2 = Factorypune()

# print(obj.a)
obj2.hello()


#syntax:-
class Parent:
    def speak(self):
        print("I can Speak!")

class Child(Parent):
    pass

#constructor and inheritance :- 
class Animal:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(f"Your name is {self.name}")

class Human(Animal):
    pass

person1 = Human("Shivam")
person1.show()
animal1 = Animal("Lion")
animal1.show()


#A case:-

class Animal:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(f"Your name is {self.name}")

class Human(Animal):
    def __init__(self, name,age):
        super().__init__(name)  #super function target parent class(Animal class)
        self.age = age

    def show(self):
            print(f"Your name is {self.name} and your age is {self.age}")

animal1 = Animal("Lion")
person2 = Human("Shivam",19)
person2.show()