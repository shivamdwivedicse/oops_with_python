class Animal:
    name = "lion" #class atribute
    
    def __init__(self , age):
        self.age = age #it is instant attribute
    
    def show(self): #it is instant methode
        print("How are you")

class Myclass:
    @classmethod  #used to create a classMethod
    def class_method(cls):
        print("This is a class method.")

class Myclass:
    @staticmethod #used to create staticMethod
    def static_method():
        print("This is a static Method.")  