# Creating a CLASS
# A class is like a blueprint or template used to create objects.
# Here "Factory" is a class that represents some kind of product (like a bag or item)
# with properties such as material, number of zips, and number of pockets.

class Factory: 
    
    # __init__ is a CONSTRUCTOR (special method)
    # It automatically runs when a new object of the class is created.
    # It is used to initialize the attributes (variables) of the object
    
    def __init__(self , material , zips, pockets):
        
        # self refers to the current object being created.
        # self.material, self.zips, self.pockets are INSTANCE VARIABLES.
        # They store data specific to each object.
        
        self.material = material   # storing material type (e.g., Leather)
        self.zips = zips           # storing number of zips
        self.pockets = pockets     # storing number of pockets
    
    # Creating a METHOD
    # A method is a function defined inside a class that operates on objects.
    # This method prints the details of the object.
    
    def show(self):
        print(f"Your object details are: {self.material},{self.zips},{self.pockets} ")

# Creating OBJECTS (instances of the class)
# Objects are real entities created using the class blueprint.

reebok = Factory("Leather" , 3 ,5)   # Object 1 → material=Leather, zips=3, pockets=5
Nike = Factory("Leather" , 5 ,8)     # Object 2 → material=Leather, zips=5, pockets=8

# Calling a METHOD using an object
# Here we call the show() method for the 'reebok' object
reebok.show()