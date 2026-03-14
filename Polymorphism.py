# # Polymorphism means "many forms" :- 
# def show():
#     print("how are you")

# def show():
#     print("you are the best")
# # when there is a function of same name another python overwrites in first function hence if i print show func. it prints you are the best
# show()



class Animal:
    def show  (self):
        print("Hello! I am Shivam.")
class Human:
    def show(self):
        print("How are you.")
obj = Animal()
obj2 = Human()

obj.show()
obj2.show() 




class Animal:
    def show2 (self):
        print("Hello! I am Shivam.")
class Human(Animal):
    def show(self):
        print("How are you.")
obj = Animal()
obj2 = Human()

obj.show2()
obj2.show() 