class Animal:
    @property  #it is a decorator
    def show(self):
        print("Hello! How are you.")
obj = Animal()
obj.show

# lets create a decorator:

def decorate(func): #func is a parameter you can wwrite any name here and func is a hello function.
    # lets create a wrapper
    def wrapper():
        print("I will print myself befoe the function hello")
        func()
        print("I will print after the function.")
    return wrapper

@decorate
def hello():
    print("Hello I am Shivam Dwivedi.")
hello()


def decorator(func):
    def wrapper(a,b):
        print("The addition of your number is :")
        func(a,b)

        print("Thankyou ! Do again")
    return wrapper

@decorator
def addition(a,b):
    print(f"Your total is {a+b}")

addition(12,13)


# *args

def decorator(func):
    def wrapper(*args):
        print("The addition of your number is :")
        func(*args)

        print("Thankyou ! Do again")
    return wrapper

@decorator
def addition(*args):
    total = sum(args)
    print(f"Your total is {total}")

addition(12,13,13,12,12,12,1,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2)


# **kwargs

def information(**kwargs):
    print("Your information is :")
    for i in kwargs:
        print(f'{i} : {kwargs[i]}')

information(name = "Shivam" , age = 19 , designation = "AI/ML")

# list comprehension:-

list_comprehension = [i for i in range(1,21) if i%2 ==0]
print(list_comprehension)

dict_comprehension = {i:i**2 for i in range(1,10)}
print(dict_comprehension)

# Lambada Functions:-
addition = lambda a,b : a+b
print(addition(12,13))

num = lambda a : "even" if a%2 ==0 else "odd"
print(num(12))

