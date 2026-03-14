# Encapsulation

# Encapsulation means putting data (variables) and code (functions)
# together in one place – inside a class.

# It also means hiding the internal details of how things work,
# and only showing what is needed.

# It keeps data safe from being changed by mistake.

# It makes your code clean and easy to use.

# It gives control over what others can access or change.

#create a protected attribute by applying _

class Factory:
    __a = "Pune"
    def __show(self):
        print("Hello! I am Pune factory.")
class Bhopal(Factory):
    def show2(self):
        print("super().a")

obj = Factory()
obj.__a


class Demo:
    def __init__(self):
        self.name="public member"   #pUBLIC
        self._age = 21           #Protected
        self.__salary = 50000   #private

    def show(self):
        print("Inside the class")
        print("Public" , self.name)
        print("Protected" , self._age)
        print("Private" , self.__salary)