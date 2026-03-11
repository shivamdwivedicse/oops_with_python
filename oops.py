class Factory:     #class is a blueprint to make objects
    a=12           #attribute

    def hello(self):   #method
        print("how are you")
    print("hello how are you i am getting initialized")    
print(Factory().a)

Factory().hello()   #use self in function to run this.


#call Factory class
obj = Factory()
# now obj is an object 

print(obj.a)
obj.hello()

obj2 =Factory()
obj3 = Factory() #obj1,obj2 are objects of Factory

# <---------------------------------------------------->