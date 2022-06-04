# python program for showcasing a method 

# class Animal is defined 
class Animal:
    def __init__(self,age,name,breed):
        self.age = age
        self.name = name
        self.breed = breed
# method is defined here
# used to define behaviors
    def bark(self):
        return "{} is now barking".format(self.name)

animal = Animal(16,max,'husky')
print(animal.age)
# print age of dog

print(animal.breed)
# breed of dog i.e husky

print(animal.name)
# print name 

