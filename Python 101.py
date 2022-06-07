# OOP IN PYTHON

# POLYMORPHISM IN PYTHON 


class Dog():
    
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        return self.name + " says woof!"

class Cat():
    
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        return self.name + " says meow"
    
dog = Dog("MAX")
cat = Cat("MILO")

print(dog.name)
print(dog.speak())

print(cat.name)
print(cat.speak())
          
    