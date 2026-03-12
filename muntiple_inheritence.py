class Animal:
    name1 = "Lion"

class Human:
    name2 = "Shivam"

class Robots(Animal,Human):  #it is called muntiple inheritence
    name3 = "charlie123"
obj = Robots()
print(obj.name1)
print(obj.name2)
print(obj.name3)
